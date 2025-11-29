import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/bmsbites.db')

def split_coffee_tea():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Find the Coffee/Tea item in Vidhyarthi Khaana (canteen_id = 1)
    cursor.execute("""
        SELECT id, name, price, category_section 
        FROM menu 
        WHERE canteen_id = 1 AND name LIKE '%Coffee/Tea%'
    """)
    item = cursor.fetchone()
    
    if item:
        item_id, name, price, section = item
        print(f"Found item: {name} (ID: {item_id}, Price: ₹{price}, Section: {section})")
        
        # Delete the combined Coffee/Tea item
        cursor.execute("DELETE FROM menu WHERE id = ?", (item_id,))
        print(f"Deleted item ID {item_id}")
        
        # Add separate Coffee and Tea items
        new_items = [
            (1, 'Coffee', 'Hot filter coffee', 10.0, 'beverage', 'hot_coffee.png', section),
            (1, 'Tea', 'Hot masala tea', 10.0, 'beverage', 'tea.png', section),
        ]
        
        cursor.executemany("""
            INSERT INTO menu (canteen_id, name, description, price, category, image_url, category_section) 
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, new_items)
        
        print(f"\nAdded 2 new items:")
        print("  - Coffee (₹10) with hot_coffee.png")
        print("  - Tea (₹10) with tea.png")
        
        conn.commit()
        
        # Verify the changes
        cursor.execute("""
            SELECT id, name, price, image_url 
            FROM menu 
            WHERE canteen_id = 1 AND (name = 'Coffee' OR name = 'Tea')
            ORDER BY name
        """)
        results = cursor.fetchall()
        print(f"\nVerification - New items in Vidhyarthi Khaana:")
        for item_id, name, price, img in results:
            print(f"  ID {item_id}: {name} - ₹{price} - {img}")
    else:
        print("No 'Coffee/Tea' item found in Vidhyarthi Khaana")
    
    conn.close()
    print("\n✓ Coffee/Tea split completed!")

if __name__ == '__main__':
    split_coffee_tea()
