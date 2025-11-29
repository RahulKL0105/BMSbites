import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/bmsbites.db')

def update_gowdas_menu():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Delete all existing menu items for Gowda's Canteen (canteen_id = 2)
    print("Deleting existing Gowda's Canteen menu items...")
    cursor.execute("DELETE FROM menu WHERE canteen_id = 2")
    print(f"Deleted {cursor.rowcount} items")
    
    # New menu items for Gowda's Canteen
    gowdas_new_menu = [
        # ENERGY ZONE
        (2, 'Red Bull Energy Drink', 'Red Bull Energy Drink', 150.0, 'beverage', 'redbull.jpg', 'ENERGY ZONE'),
        (2, 'Red Bull Sugar Free', 'Red Bull Sugar Free', 150.0, 'beverage', 'redbull.jpg', 'ENERGY ZONE'),
        (2, 'Red Bull Yellow Edition', 'Red Bull Yellow Edition', 175.0, 'beverage', 'redbull.jpg', 'ENERGY ZONE'),
        
        # ROLLS
        (2, 'Veg Roll', 'Veg Roll', 45.0, 'veg', 'frankie.jpg', 'ROLLS'),
        (2, 'Veg Roll with Cheese', 'Veg Roll with Cheese', 65.0, 'veg', 'frankie.jpg', 'ROLLS'),
        (2, 'Egg Roll', 'Egg Roll', 55.0, 'non-veg', 'egg_burji.jpg', 'ROLLS'),
        (2, 'Egg Roll with Cheese', 'Egg Roll with Cheese', 75.0, 'non-veg', 'egg_burji.jpg', 'ROLLS'),
        (2, 'Chicken Roll', 'Chicken Roll', 75.0, 'non-veg', 'frankie.jpg', 'ROLLS'),
        (2, 'Chicken Roll with Cheese', 'Chicken Roll with Cheese', 95.0, 'non-veg', 'frankie.jpg', 'ROLLS'),
        (2, 'Paneer Roll', 'Paneer Roll', 65.0, 'veg', 'frankie.jpg', 'ROLLS'),
        (2, 'Paneer Roll with Cheese', 'Paneer Roll with Cheese', 87.0, 'veg', 'frankie.jpg', 'ROLLS'),
        (2, 'Mushroom Roll', 'Mushroom Roll', 75.0, 'veg', 'frankie.jpg', 'ROLLS'),
        (2, 'Mushroom Roll with Cheese', 'Mushroom Roll with Cheese', 95.0, 'veg', 'frankie.jpg', 'ROLLS'),
        
        # MASALA MAGGI
        (2, 'Masala Cooking Maggi', 'Masala Cooking Maggi', 35.0, 'veg', 'maggie.jpg', 'MASALA MAGGI'),
        (2, 'Masala Cooking Maggi Cheese', 'Masala Cooking Maggi Cheese', 50.0, 'veg', 'maggie.jpg', 'MASALA MAGGI'),
        (2, 'Egg Masala Maggi', 'Egg Masala Maggi', 50.0, 'non-veg', 'maggie.jpg', 'MASALA MAGGI'),
        (2, 'Egg Masala Maggi Cheese', 'Egg Masala Maggi Cheese', 65.0, 'non-veg', 'maggie.jpg', 'MASALA MAGGI'),
        (2, 'Paneer Masala Maggi', 'Paneer Masala Maggi', 65.0, 'veg', 'maggie.jpg', 'MASALA MAGGI'),
        (2, 'Paneer Masala Maggi Cheese', 'Paneer Masala Maggi Cheese', 75.0, 'veg', 'maggie.jpg', 'MASALA MAGGI'),
        (2, 'Chicken Masala Maggi', 'Chicken Masala Maggi', 75.0, 'non-veg', 'maggie.jpg', 'MASALA MAGGI'),
        (2, 'Chicken Masala Maggi Cheese', 'Chicken Masala Maggi Cheese', 97.0, 'non-veg', 'maggie.jpg', 'MASALA MAGGI'),
        
        # WAI WAI MAGGI
        (2, 'Veg Wai Wai Maggi Masala', 'Veg Wai Wai Maggi Masala', 40.0, 'veg', 'maggie.jpg', 'WAI WAI MAGGI'),
        (2, 'Veg Wai Wai Maggi Masala Cheese', 'Veg Wai Wai Maggi Masala Cheese', 55.0, 'veg', 'maggie.jpg', 'WAI WAI MAGGI'),
        (2, 'Chicken Wai Wai Maggi', 'Chicken Wai Wai Maggi', 50.0, 'non-veg', 'maggie.jpg', 'WAI WAI MAGGI'),
        (2, 'Chicken Wai Wai Maggi with Cheese', 'Chicken Wai Wai Maggi with Cheese', 65.0, 'non-veg', 'maggie.jpg', 'WAI WAI MAGGI'),
        
        # PASTA / MAGGI PASTA
        (2, 'Tomato Pasta', 'Tomato Pasta', 58.0, 'veg', 'noodles.jpg', 'PASTA / MAGGI PASTA'),
        (2, 'Masala Pasta', 'Masala Pasta', 58.0, 'veg', 'noodles.jpg', 'PASTA / MAGGI PASTA'),
        (2, 'Mushroom Pasta', 'Mushroom Pasta', 58.0, 'veg', 'noodles.jpg', 'PASTA / MAGGI PASTA'),
        (2, 'Cheese Pasta', 'Cheese Pasta', 78.0, 'veg', 'noodles.jpg', 'PASTA / MAGGI PASTA'),
        (2, 'Extra Cheese', 'Extra Cheese', 20.0, 'veg', 'cheese.jpg', 'PASTA / MAGGI PASTA'),
        
        # HOT DOGS
        (2, 'Veg Hot Dog', 'Veg Hot Dog', 35.0, 'veg', 'burger.jpg', 'HOT DOGS'),
        (2, 'Veg Hot Dog Cheese', 'Veg Hot Dog Cheese', 45.0, 'veg', 'burger.jpg', 'HOT DOGS'),
        (2, 'Veg Hot Dog Cheese + Chips', 'Veg Hot Dog Cheese + Chips', 65.0, 'veg', 'burger.jpg', 'HOT DOGS'),
        (2, 'Veg Paneer Hot Dog', 'Veg Paneer Hot Dog', 55.0, 'veg', 'burger.jpg', 'HOT DOGS'),
        (2, 'Veg Paneer Hot Dog Cheese', 'Veg Paneer Hot Dog Cheese', 65.0, 'veg', 'burger.jpg', 'HOT DOGS'),
        (2, 'Veg Hot Dog Omelette', 'Veg Hot Dog Omelette', 55.0, 'non-veg', 'burger.jpg', 'HOT DOGS'),
        (2, 'Chicken Hot Dog', 'Chicken Hot Dog', 65.0, 'non-veg', 'burger.jpg', 'HOT DOGS'),
        (2, 'Chicken Hot Dog Cheese', 'Chicken Hot Dog Cheese', 75.0, 'non-veg', 'burger.jpg', 'HOT DOGS'),
        (2, 'Chicken Hot Dog Cheese + Chips', 'Chicken Hot Dog Cheese + Chips', 87.0, 'non-veg', 'burger.jpg', 'HOT DOGS'),
        
        # EGG ITEMS
        (2, 'Bun Omelette Plain', 'Bun Omelette Plain', 35.0, 'non-veg', 'plain_omelette.jpg', 'EGG ITEMS'),
        (2, 'Bun Omelette Cheese & Chips', 'Bun Omelette Cheese & Chips', 65.0, 'non-veg', 'cheese_omelette.jpg', 'EGG ITEMS'),
        (2, 'Bread Omelette Plain', 'Bread Omelette Plain', 25.0, 'non-veg', 'bread_omelette.jpg', 'EGG ITEMS'),
        (2, 'Single Omelette', 'Single Omelette', 20.0, 'non-veg', 'plain_omelette.jpg', 'EGG ITEMS'),
        (2, 'Double Omelette', 'Double Omelette', 25.0, 'non-veg', 'plain_omelette.jpg', 'EGG ITEMS'),
        (2, 'Egg Puff', 'Egg Puff', 25.0, 'non-veg', 'puff.jpg', 'EGG ITEMS'),
        (2, 'Egg Puff Cheese', 'Egg Puff Cheese', 35.0, 'non-veg', 'puff.jpg', 'EGG ITEMS'),
        (2, 'Bun Butter Egg Puff', 'Bun Butter Egg Puff', 45.0, 'non-veg', 'puff.jpg', 'EGG ITEMS'),
        (2, 'Bun Butter Egg Puff Cheese', 'Bun Butter Egg Puff Cheese', 55.0, 'non-veg', 'puff.jpg', 'EGG ITEMS'),
        
        # BURGER
        (2, 'Veg Burger Plain', 'Veg Burger Plain', 35.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Veg Burger Cheese', 'Veg Burger Cheese', 50.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Veg Burger Cheese + Chips', 'Veg Burger Cheese + Chips', 50.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Paneer Burger', 'Paneer Burger', 50.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Paneer Burger Cheese', 'Paneer Burger Cheese', 65.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Chicken Burger', 'Chicken Burger', 75.0, 'non-veg', 'burger.jpg', 'BURGER'),
        (2, 'Chicken Burger with Cheese', 'Chicken Burger with Cheese', 87.0, 'non-veg', 'burger.jpg', 'BURGER'),
        
        # MAGGI SPECIAL
        (2, 'Veg Fried Maggi', 'Veg Fried Maggi', 55.0, 'veg', 'maggie.jpg', 'MAGGI SPECIAL'),
        (2, 'Veg Fried Maggi Cheese', 'Veg Fried Maggi Cheese', 65.0, 'veg', 'maggie.jpg', 'MAGGI SPECIAL'),
        (2, 'Chicken Fried Maggi', 'Chicken Fried Maggi', 75.0, 'non-veg', 'maggie.jpg', 'MAGGI SPECIAL'),
        (2, 'Chicken Fried Maggi Cheese', 'Chicken Fried Maggi Cheese', 87.0, 'non-veg', 'maggie.jpg', 'MAGGI SPECIAL'),
        (2, 'Egg Fried Maggi', 'Egg Fried Maggi', 55.0, 'non-veg', 'maggie.jpg', 'MAGGI SPECIAL'),
        (2, 'Egg Fried Maggi Cheese', 'Egg Fried Maggi Cheese', 65.0, 'non-veg', 'maggie.jpg', 'MAGGI SPECIAL'),
        
        # SAMOSA
        (2, 'Samosa', 'Samosa', 20.0, 'veg', 'samosa.jpg', 'SAMOSA'),
        (2, 'Samosa Chat Masala', 'Samosa Chat Masala', 40.0, 'veg', 'samosa_chat.jpg', 'SAMOSA'),
        (2, 'Bun Samosa Plain', 'Bun Samosa Plain', 30.0, 'veg', 'samosa.jpg', 'SAMOSA'),
        (2, 'Bun Samosa Cheese', 'Bun Samosa Cheese', 45.0, 'veg', 'samosa.jpg', 'SAMOSA'),
        
        # PUFFS
        (2, 'Veg Puff', 'Veg Puff', 25.0, 'veg', 'puff.jpg', 'PUFFS'),
        (2, 'Veg Puff Cheese', 'Veg Puff Cheese', 35.0, 'veg', 'puff.jpg', 'PUFFS'),
        (2, 'Bun Veg Puff', 'Bun Veg Puff', 45.0, 'veg', 'puff.jpg', 'PUFFS'),
        (2, 'Bun Veg Puff Cheese', 'Bun Veg Puff Cheese', 55.0, 'veg', 'puff.jpg', 'PUFFS'),
        (2, 'Paneer Puff', 'Paneer Puff', 50.0, 'veg', 'puff.jpg', 'PUFFS'),
        (2, 'Paneer Puff Cheese', 'Paneer Puff Cheese', 60.0, 'veg', 'puff.jpg', 'PUFFS'),
        (2, 'Paneer Puff Cheese + Chips', 'Paneer Puff Cheese + Chips', 75.0, 'veg', 'puff.jpg', 'PUFFS'),
        (2, 'Chicken Puff', 'Chicken Puff', 50.0, 'non-veg', 'puff.jpg', 'PUFFS'),
        (2, 'Chicken Puff Cheese', 'Chicken Puff Cheese', 60.0, 'non-veg', 'puff.jpg', 'PUFFS'),
        (2, 'Chicken Puff Cheese + Chips', 'Chicken Puff Cheese + Chips', 80.0, 'non-veg', 'puff.jpg', 'PUFFS'),
        
        # MOMOS
        (2, 'Veg Momos', 'Veg Momos', 65.0, 'veg', 'momos.jpg', 'MOMOS'),
        (2, 'Chicken Momos', 'Chicken Momos', 75.0, 'non-veg', 'momos.jpg', 'MOMOS'),
        
        # BUN SECTION
        (2, 'Bun Butter Jam', 'Bun Butter Jam', 25.0, 'veg', 'buns.jpg', 'BUN SECTION'),
        (2, 'Bun Butter Jam Bread Toast', 'Bun Butter Jam Bread Toast', 30.0, 'veg', 'buns.jpg', 'BUN SECTION'),
        (2, 'Bun Masala', 'Bun Masala', 35.0, 'veg', 'buns.jpg', 'BUN SECTION'),
        (2, 'Bun Masala Cheese', 'Bun Masala Cheese', 45.0, 'veg', 'buns.jpg', 'BUN SECTION'),
        
        # SOFT DRINKS & BEVERAGES
        (2, 'Coca Cola', 'Coca Cola', 20.0, 'beverage', 'coke.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Thumbs Up', 'Thumbs Up', 20.0, 'beverage', 'coke.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Mountain Dew', 'Mountain Dew', 20.0, 'beverage', 'coke.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Sprite', 'Sprite', 20.0, 'beverage', 'coke.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Paper Boat', 'Paper Boat', 25.0, 'beverage', 'juice.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Tropical Juice / Fruit Mix', 'Tropical Juice / Fruit Mix', 25.0, 'beverage', 'juice.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Fresh Juices', 'Fresh Juices', 40.0, 'beverage', 'juice.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Lime Juice', 'Lime Juice', 20.0, 'beverage', 'juice.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Grape Juice', 'Grape Juice', 20.0, 'beverage', 'juice.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Hot Coffee', 'Hot Coffee', 20.0, 'beverage', 'coffee.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Tea / Lemon Tea', 'Tea / Lemon Tea', 15.0, 'beverage', 'coffee.jpg', 'SOFT DRINKS & BEVERAGES'),
    ]
    
    print(f"\nInserting {len(gowdas_new_menu)} new menu items...")
    cursor.executemany("""
        INSERT INTO menu (canteen_id, name, description, price, category, image_url, category_section) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, gowdas_new_menu)
    
    conn.commit()
    
    # Verify the changes
    cursor.execute("SELECT COUNT(*) FROM menu WHERE canteen_id = 2")
    count = cursor.fetchone()[0]
    print(f"\nTotal menu items for Gowda's Canteen: {count}")
    
    cursor.execute("SELECT DISTINCT category_section FROM menu WHERE canteen_id = 2 ORDER BY category_section")
    sections = cursor.fetchall()
    print(f"\nMenu sections ({len(sections)}):")
    for section in sections:
        cursor.execute("SELECT COUNT(*) FROM menu WHERE canteen_id = 2 AND category_section = ?", (section[0],))
        item_count = cursor.fetchone()[0]
        print(f"  - {section[0]}: {item_count} items")
    
    conn.close()
    print("\n✓ Gowda's Canteen menu updated successfully!")

if __name__ == '__main__':
    update_gowdas_menu()
