import pandas as pd
import numpy as np
import sqlite3
from config import Config

class AnalyticsManager:
    def __init__(self, db_path=None):
        self.db_path = db_path or Config.DATABASE

    def get_orders_df(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM orders", conn)
        conn.close()
        return df

    def get_order_items_df(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM order_items", conn)
        conn.close()
        return df
    
    def get_menu_df(self):
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM menu", conn)
        conn.close()
        return df

    def get_sales_summary(self):
        """Calculates total sales, order count, avg order value."""
        orders = self.get_orders_df()
        if orders.empty:
            return {'total_revenue': 0, 'total_orders': 0, 'avg_order_value': 0}
        
        total_revenue = np.sum(orders['total_amount'])
        total_orders = len(orders)
        avg_order_value = np.mean(orders['total_amount'])
        
        return {
            'total_revenue': round(total_revenue, 2),
            'total_orders': total_orders,
            'avg_order_value': round(avg_order_value, 2)
        }

    def get_top_selling_items(self, n=5):
        """Finds top N selling items."""
        items = self.get_order_items_df()
        menu = self.get_menu_df()
        
        if items.empty:
            return []

        # Merge with menu to get names
        merged = pd.merge(items, menu, left_on='menu_id', right_on='id')
        
        # Group by item name and sum quantity
        top_items = merged.groupby('name')['quantity'].sum().sort_values(ascending=False).head(n)
        
        return top_items.to_dict()

    def get_daily_revenue(self):
        """Calculates daily revenue."""
        orders = self.get_orders_df()
        if orders.empty:
            return {}
            
        orders['created_at'] = pd.to_datetime(orders['created_at'])
        daily = orders.groupby(orders['created_at'].dt.date)['total_amount'].sum()
        return daily.to_dict()

    def get_recommendations(self, current_cart_item_ids):
        """Simple recommendation engine: 'Users who bought X also bought Y'."""
        # This is a simplified version. A real one would use a co-occurrence matrix.
        # For now, we'll just return top selling items that are NOT in the cart.
        
        top_items = self.get_top_selling_items(n=10)
        recommendations = []
        
        # Handle case when top_items is empty list (no orders yet)
        if not top_items:
            # Return random menu items instead
            menu = self.get_menu_df()
            if not menu.empty:
                sample = menu[menu['is_available'] == 1].sample(min(3, len(menu)))
                return sample.to_dict('records')
            return []
        
        for name, qty in top_items.items():
            # Find menu_id for this name
            menu = self.get_menu_df()
            item_row = menu[menu['name'] == name]
            if not item_row.empty:
                item_dict = item_row.iloc[0].to_dict()
                if item_dict['id'] not in current_cart_item_ids:
                    recommendations.append(item_dict)
                    if len(recommendations) >= 3:
                        break
        
        return recommendations

