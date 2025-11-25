from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from utils.menu_manager import MenuManager
from utils.analytics import AnalyticsManager
from utils.order_manager import OrderManager
import functools

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')
menu_mgr = MenuManager()
analytics_mgr = AnalyticsManager()
order_mgr = OrderManager()

def admin_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if session.get('role') != 'admin':
            flash('Admin access required', 'danger')
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    summary = analytics_mgr.get_sales_summary()
    top_items = analytics_mgr.get_top_selling_items()
    daily_rev = analytics_mgr.get_daily_revenue()
    recent_orders = order_mgr.get_all_orders()[:10] # Last 10 orders
    
    return render_template('dashboard.html', 
                           summary=summary, 
                           top_items=top_items, 
                           daily_rev=daily_rev,
                           recent_orders=recent_orders)

@admin_bp.route('/menu')
@admin_required
def manage_menu():
    menu_items = menu_mgr.get_menu_df().to_dict('records')
    canteens = menu_mgr.get_canteens()
    return render_template('manage_menu.html', menu_items=menu_items, canteens=canteens)

@admin_bp.route('/menu/add', methods=['POST'])
@admin_required
def add_item():
    menu_mgr.add_item(
        int(request.form['canteen_id']),
        request.form['name'],
        request.form['description'],
        float(request.form['price']),
        request.form['category'],
        request.form['image_url']
    )
    flash('Item added', 'success')
    return redirect(url_for('admin.manage_menu'))

@admin_bp.route('/menu/edit/<int:item_id>', methods=['POST'])
@admin_required
def edit_item(item_id):
    menu_mgr.update_item(
        item_id,
        int(request.form['canteen_id']),
        request.form['name'],
        request.form['description'],
        float(request.form['price']),
        request.form['category'],
        request.form['image_url'],
        1 if 'is_available' in request.form else 0
    )
    flash('Item updated', 'success')
    return redirect(url_for('admin.manage_menu'))

@admin_bp.route('/menu/delete/<int:item_id>')
@admin_required
def delete_item(item_id):
    menu_mgr.delete_item(item_id)
    flash('Item deleted', 'success')
    return redirect(url_for('admin.manage_menu'))

@admin_bp.route('/orders')
@admin_required
def manage_orders():
    orders = order_mgr.get_all_orders()
    return render_template('manage_orders.html', orders=orders)

@admin_bp.route('/order/status/<int:order_id>', methods=['POST'])
@admin_required
def update_status(order_id):
    status = request.form['status']
    order_mgr.update_order_status(order_id, status)
    flash('Order status updated', 'success')
    return redirect(url_for('admin.manage_orders'))
