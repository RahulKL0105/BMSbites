import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/bmsbites.db')

def update_menu_images():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Update Coffee/Tea items
    print("Updating Coffee/Tea images...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'hot_coffee.png' 
        WHERE name LIKE '%Coffee/Tea%' OR name LIKE '%Hot Coffee%'
    """)
    print(f"  Updated {cursor.rowcount} coffee items")
    
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'tea.png' 
        WHERE (name LIKE '%Tea%' OR name LIKE '%Lemon Tea%') 
        AND name NOT LIKE '%Coffee%'
    """)
    print(f"  Updated {cursor.rowcount} tea items")
    
    # Update Cold Coffee
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'cold_coffee.png' 
        WHERE name LIKE '%Cold Coffee%'
    """)
    print(f"  Updated {cursor.rowcount} cold coffee items")
    
    # Update Vada items (single vada)
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'vada_single.png' 
        WHERE name LIKE 'Vada (1)%' OR name = 'Vada (1)'
    """)
    print(f"  Updated {cursor.rowcount} single vada items")
    
    # Update Idly + Vada combo items
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'idly_vada_combo.png' 
        WHERE name LIKE '%Idly%Vada%' OR name LIKE 'Idly (2) + Vada (1)' OR name LIKE 'Idly (1) + Vada (1)'
    """)
    print(f"  Updated {cursor.rowcount} idly+vada combo items")
    
    conn.commit()
    
    # Verify changes
    print("\n=== Verification ===")
    cursor.execute("SELECT name, image_url FROM menu WHERE image_url IN ('hot_coffee.png', 'tea.png', 'cold_coffee.png', 'vada_single.png', 'idly_vada_combo.png') ORDER BY name")
    results = cursor.fetchall()
    print(f"\nTotal items updated: {len(results)}")
    for item_name, img in results:
        print(f"  - {item_name}: {img}")
    
    conn.close()
    print("\n✓ Menu images updated successfully!")

if __name__ == '__main__':
    update_menu_images()
