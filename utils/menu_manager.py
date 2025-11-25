import pandas as pd
import sqlite3
from config import Config

class MenuManager:
    def __init__(self, db_path=None):
        self.db_path = db_path or Config.DATABASE

    def get_canteens(self):
        """Get all canteens."""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM canteens WHERE is_open=1", conn)
        conn.close()
        return df.to_dict('records')

    def get_canteen(self, canteen_id):
        """Get single canteen."""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM canteens WHERE id=?", conn, params=(canteen_id,))
        conn.close()
        if not df.empty:
            return df.iloc[0].to_dict()
        return None

    def get_menu_df(self, canteen_id=None):
        """Reads menu from SQLite into a Pandas DataFrame."""
        conn = sqlite3.connect(self.db_path)
        if canteen_id:
            df = pd.read_sql_query("SELECT * FROM menu WHERE canteen_id=?", conn, params=(canteen_id,))
        else:
            df = pd.read_sql_query("SELECT * FROM menu", conn)
        conn.close()
        return df

    def get_filtered_menu(self, canteen_id=None, category=None, min_price=0, max_price=1000, sort_by='name'):
        """Filters and sorts menu using Pandas."""
        df = self.get_menu_df(canteen_id)
        
        # Filter by availability
        df = df[df['is_available'] == 1]

        # Filter by category
        if category and category != 'all':
            df = df[df['category'] == category]
        
        # Filter by price
        df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]

        # Sort
        if sort_by == 'price_asc':
            df = df.sort_values(by='price', ascending=True)
        elif sort_by == 'price_desc':
            df = df.sort_values(by='price', ascending=False)
        else:
            df = df.sort_values(by='name')

        return df.to_dict('records')
    
    def get_menu_by_section(self, canteen_id=None, category=None, search=None):
        """Get menu items grouped by category_section."""
        df = self.get_menu_df(canteen_id)
        
        # Filter by availability
        df = df[df['is_available'] == 1]
        
        # Filter by category if specified
        if category and category != 'all':
            df = df[df['category'] == category]
        
        # Filter by search term if specified
        if search:
            df = df[df['name'].str.contains(search, case=False, na=False)]
        
        # Group by category_section
        grouped = {}
        for section in df['category_section'].unique():
            if pd.notna(section):  # Skip null sections
                section_items = df[df['category_section'] == section].to_dict('records')
                grouped[section] = section_items
        
        return grouped


    def add_item(self, canteen_id, name, description, price, category, image_url):
        """Adds a new item to the menu."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO menu (canteen_id, name, description, price, category, image_url) VALUES (?, ?, ?, ?, ?, ?)",
                       (canteen_id, name, description, price, category, image_url))
        conn.commit()
        conn.close()

    def update_item(self, item_id, canteen_id, name, description, price, category, image_url, is_available):
        """Updates an existing item."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            UPDATE menu 
            SET canteen_id=?, name=?, description=?, price=?, category=?, image_url=?, is_available=?
            WHERE id=?
        """, (canteen_id, name, description, price, category, image_url, is_available, item_id))
        conn.commit()
        conn.close()

    def delete_item(self, item_id):
        """Deletes an item."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM menu WHERE id=?", (item_id,))
        conn.commit()
        conn.close()

    def get_item(self, item_id):
        """Get single item."""
        conn = sqlite3.connect(self.db_path)
        df = pd.read_sql_query("SELECT * FROM menu WHERE id=?", conn, params=(item_id,))
        conn.close()
        if not df.empty:
            return df.iloc[0].to_dict()
        return None
