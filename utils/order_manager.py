import sqlite3
from config import Config
import pandas as pd
from datetime import datetime, timedelta

class OrderManager:
    def __init__(self, db_path=None):
        self.db_path = db_path or Config.DATABASE

    def create_order(self, user_id, canteen_id, cart_items, pickup_time=None):
        """Creates an order and order items."""
        # cart_items is a list of dicts: {'menu_id': 1, 'quantity': 2, 'price': 50}
        
        total_amount = sum(item['price'] * item['quantity'] for item in cart_items)
        
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO orders (user_id, canteen_id, total_amount, status, pickup_time) VALUES (?, ?, ?, ?, ?)",
                       (user_id, canteen_id, total_amount, 'preparing', pickup_time))
        order_id = cursor.lastrowid
        
        for item in cart_items:
            cursor.execute("INSERT INTO order_items (order_id, menu_id, quantity, price_at_order) VALUES (?, ?, ?, ?)",
                           (order_id, item['menu_id'], item['quantity'], item['price']))
            
        conn.commit()
        conn.close()
        return order_id

    def get_user_orders(self, user_id):
        """Get all orders for a user with auto-updated status."""
        conn = sqlite3.connect(self.db_path)
        orders = pd.read_sql_query("SELECT * FROM orders WHERE user_id=? ORDER BY created_at DESC", conn, params=(user_id,))
        
        # Auto-update status based on time
        cursor = conn.cursor()
        for idx, order in orders.iterrows():
            if order['status'] == 'preparing':
                # Check if 5 minutes have passed
                created_at = datetime.strptime(order['created_at'], '%Y-%m-%d %H:%M:%S')
                time_diff = datetime.now() - created_at
                if time_diff >= timedelta(minutes=5):
                    # Update to ready
                    cursor.execute("UPDATE orders SET status='ready' WHERE id=?", (order['id'],))
                    orders.at[idx, 'status'] = 'ready'
        
        conn.commit()
        conn.close()
        return orders.to_dict('records')

    def get_order_details(self, order_id):
        """Get details of a specific order with auto-updated status."""
        conn = sqlite3.connect(self.db_path)
        order = pd.read_sql_query("SELECT * FROM orders WHERE id=?", conn, params=(order_id,))
        
        # Auto-update status if needed
        if not order.empty and order.iloc[0]['status'] == 'preparing':
            created_at = datetime.strptime(order.iloc[0]['created_at'], '%Y-%m-%d %H:%M:%S')
            time_diff = datetime.now() - created_at
            if time_diff >= timedelta(minutes=5):
                cursor = conn.cursor()
                cursor.execute("UPDATE orders SET status='ready' WHERE id=?", (order_id,))
                conn.commit()
                order.at[0, 'status'] = 'ready'
        
        items = pd.read_sql_query("""
            SELECT oi.*, m.name, m.image_url 
            FROM order_items oi 
            JOIN menu m ON oi.menu_id = m.id 
            WHERE oi.order_id=?
        """, conn, params=(order_id,))
        conn.close()
        
        if order.empty:
            return None
            
        return {
            'order': order.iloc[0].to_dict(),
            'items': items.to_dict('records')
        }

    def update_order_status(self, order_id, status):
        """Update order status."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE orders SET status=? WHERE id=?", (status, order_id))
        conn.commit()
        conn.close()

    def get_all_orders(self):
        """Get all orders for admin with auto-updated status."""
        conn = sqlite3.connect(self.db_path)
        orders = pd.read_sql_query("""
            SELECT o.*, u.username, c.name as canteen_name
            FROM orders o 
            JOIN users u ON o.user_id = u.id 
            JOIN canteens c ON o.canteen_id = c.id
            ORDER BY o.created_at DESC
        """, conn)
        
        # Auto-update status based on time
        cursor = conn.cursor()
        for idx, order in orders.iterrows():
            if order['status'] == 'preparing':
                created_at = datetime.strptime(order['created_at'], '%Y-%m-%d %H:%M:%S')
                time_diff = datetime.now() - created_at
                if time_diff >= timedelta(minutes=5):
                    cursor.execute("UPDATE orders SET status='ready' WHERE id=?", (order['id'],))
                    orders.at[idx, 'status'] = 'ready'
        
        conn.commit()
        conn.close()
        return orders.to_dict('records')
