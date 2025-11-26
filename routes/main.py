from flask import Blueprint, render_template, request, redirect, url_for, flash, session, jsonify
from utils.menu_manager import MenuManager
from utils.order_manager import OrderManager
from utils.analytics import AnalyticsManager
import sqlite3
from config import Config

main_bp = Blueprint('main', __name__)
menu_mgr = MenuManager()
order_mgr = OrderManager()
analytics_mgr = AnalyticsManager()

@main_bp.route('/')
def index():
    canteens = menu_mgr.get_canteens()
    return render_template('index.html', canteens=canteens)

@main_bp.route('/canteens')
def canteens():
    canteens_list = menu_mgr.get_canteens()
    return render_template('canteens.html', canteens=canteens_list)

@main_bp.route('/select_canteen/<int:canteen_id>')
def select_canteen(canteen_id):
    session['canteen_id'] = canteen_id
    canteen = menu_mgr.get_canteen(canteen_id)
    if canteen:
        flash(f"Selected {canteen['name']}", 'success')
    return redirect(url_for('main.menu'))

@main_bp.route('/menu')
def menu():
    canteen_id = session.get('canteen_id')
    if not canteen_id:
        flash('Please select a canteen first', 'warning')
        return redirect(url_for('main.canteens'))
    
    category = request.args.get('category', 'all')
    search = request.args.get('search', '')
    menu_sections = menu_mgr.get_menu_by_section(canteen_id=canteen_id, category=category, search=search)
    canteen = menu_mgr.get_canteen(canteen_id)
    return render_template('menu.html', menu_sections=menu_sections, category=category, search=search, canteen=canteen)

@main_bp.route('/cart')
def cart():
    cart_ids = session.get('cart', {})
    cart_items = []
    total = 0
    
    for item_id, qty in cart_ids.items():
        item = menu_mgr.get_item(item_id)
        if item:
            item['quantity'] = qty
            item['total'] = item['price'] * qty
            cart_items.append(item)
            total += item['total']
            
    # Calculate Platform & Preorder Fee (2%)
    platform_fee = round(total * 0.02, 2)
    grand_total = total + platform_fee
            
    # Get recommendations based on cart
    recommendations = analytics_mgr.get_recommendations(list(cart_ids.keys()))
            
    return render_template('cart.html', cart_items=cart_items, subtotal=total, platform_fee=platform_fee, total=grand_total, recommendations=recommendations)

@main_bp.route('/add_to_cart/<int:item_id>', methods=['POST'])
def add_to_cart(item_id):
    if 'cart' not in session:
        session['cart'] = {}
    
    cart = session['cart']
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    session.modified = True
    
    flash('Item added to cart', 'success')
    return redirect(url_for('main.menu'))

@main_bp.route('/update_cart/<int:item_id>', methods=['POST'])
def update_cart(item_id):
    action = request.form.get('action')
    cart = session.get('cart', {})
    
    if str(item_id) in cart:
        if action == 'increase':
            cart[str(item_id)] += 1
        elif action == 'decrease':
            cart[str(item_id)] -= 1
            if cart[str(item_id)] <= 0:
                del cart[str(item_id)]
        elif action == 'remove':
            del cart[str(item_id)]
            
    session.modified = True
    return redirect(url_for('main.cart'))

@main_bp.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if 'user_id' not in session:
        flash('Please login to checkout', 'warning')
        return redirect(url_for('auth.login'))
    
    canteen_id = session.get('canteen_id')
    if not canteen_id:
        flash('Please select a canteen', 'warning')
        return redirect(url_for('main.canteens'))
        
    cart_ids = session.get('cart', {})
    if not cart_ids:
        flash('Cart is empty', 'warning')
        return redirect(url_for('main.menu'))
        
    if request.method == 'POST':
        # Get pickup time from form
        pickup_time = request.form.get('pickup_time')
        if not pickup_time:
            flash('Please select a pickup time', 'warning')
            return redirect(url_for('main.checkout'))
        
        # Process order
        cart_items_data = []
        total_items_price = 0
        for item_id, qty in cart_ids.items():
            item = menu_mgr.get_item(item_id)
            if item:
                item_total = item['price'] * qty
                total_items_price += item_total
                cart_items_data.append({
                    'menu_id': item['id'],
                    'quantity': qty,
                    'price': item['price']
                })
        
        # Calculate fee again for security
        platform_fee = round(total_items_price * 0.02, 2)
        
        order_id = order_mgr.create_order(session['user_id'], canteen_id, cart_items_data, pickup_time, platform_fee)
        session['cart'] = {} # Clear cart
        flash(f'Order #{order_id} placed successfully! Pickup time: {pickup_time}', 'success')
        return redirect(url_for('main.orders'))
    
    # Calculate totals for display
    total_items_price = 0
    for item_id, qty in cart_ids.items():
        item = menu_mgr.get_item(item_id)
        if item:
            total_items_price += item['price'] * qty
            
    platform_fee = round(total_items_price * 0.02, 2)
    grand_total = total_items_price + platform_fee
    
    # Generate time slots from 9:00 AM to 5:30 PM in 20-minute intervals
    time_slots = []
    start_hour = 9
    start_minute = 0
    end_hour = 17
    end_minute = 30
    
    current_hour = start_hour
    current_minute = start_minute
    
    while (current_hour < end_hour) or (current_hour == end_hour and current_minute <= end_minute):
        # Calculate end time for this slot (20 minutes later)
        end_slot_minute = current_minute + 20
        end_slot_hour = current_hour
        if end_slot_minute >= 60:
            end_slot_minute -= 60
            end_slot_hour += 1
        
        # Format start time
        start_period = 'AM' if current_hour < 12 else 'PM'
        start_display_hour = current_hour if current_hour <= 12 else current_hour - 12
        if start_display_hour == 0:
            start_display_hour = 12
        
        # Format end time
        end_period = 'AM' if end_slot_hour < 12 else 'PM'
        end_display_hour = end_slot_hour if end_slot_hour <= 12 else end_slot_hour - 12
        if end_display_hour == 0:
            end_display_hour = 12
        
        # Create interval format: "9:00-9:20 AM" or "11:40 AM-12:00 PM"
        if start_period == end_period:
            time_slot = f"{start_display_hour}:{current_minute:02d}-{end_display_hour}:{end_slot_minute:02d} {end_period}"
        else:
            time_slot = f"{start_display_hour}:{current_minute:02d} {start_period}-{end_display_hour}:{end_slot_minute:02d} {end_period}"
        
        time_slots.append(time_slot)
        
        # Move to next slot
        current_minute += 20
        if current_minute >= 60:
            current_minute -= 60
            current_hour += 1
        
    return render_template('checkout.html', time_slots=time_slots, subtotal=total_items_price, platform_fee=platform_fee, total=grand_total)

@main_bp.route('/orders')
def orders():
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    user_orders = order_mgr.get_user_orders(session['user_id'])
    return render_template('orders.html', orders=user_orders)

@main_bp.route('/order/<int:order_id>')
def order_detail(order_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
        
    details = order_mgr.get_order_details(order_id)
    if not details or details['order']['user_id'] != session['user_id']:
        flash('Order not found', 'danger')
        return redirect(url_for('main.orders'))
        
    return render_template('order_detail.html', **details)

@main_bp.route('/receipt/<int:order_id>')
def view_receipt(order_id):
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))
    
    # Get order details
    details = order_mgr.get_order_details(order_id)
    if not details or details['order']['user_id'] != session['user_id']:
        flash('Order not found', 'danger')
        return redirect(url_for('main.orders'))
    
    # Get username
    conn = sqlite3.connect(Config.DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE id=?", (session['user_id'],))
    user = cursor.fetchone()
    username = user[0] if user else 'Guest'
    
    # Get canteen name
    cursor.execute("SELECT name FROM canteens WHERE id=?", (details['order']['canteen_id'],))
    canteen = cursor.fetchone()
    canteen_name = canteen[0] if canteen else 'Unknown Canteen'
    conn.close()
    
    return render_template('receipt.html', 
                         order=details['order'], 
                         items=details['items'],
                         username=username,
                         canteen_name=canteen_name)
