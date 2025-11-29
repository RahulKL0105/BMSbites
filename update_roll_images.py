import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/bmsbites.db')

def update_roll_images():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Update Red Bull items
    print("Updating Red Bull images...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'redbull_new.png' 
        WHERE name LIKE '%Red Bull%'
    """)
    print(f"  Updated {cursor.rowcount} Red Bull items")
    
    # Update Veg Roll items
    print("\nUpdating Veg Roll images...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'veg_roll_new.png' 
        WHERE name LIKE '%Veg Roll%'
    """)
    print(f"  Updated {cursor.rowcount} Veg Roll items")
    
    # Update Egg Roll items
    print("\nUpdating Egg Roll images...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'egg_roll_new.png' 
        WHERE name LIKE '%Egg Roll%'
    """)
    print(f"  Updated {cursor.rowcount} Egg Roll items")
    
    # Update Paneer Roll items
    print("\nUpdating Paneer Roll images...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'paneer_roll_new.png' 
        WHERE name LIKE '%Paneer Roll%'
    """)
    print(f"  Updated {cursor.rowcount} Paneer Roll items")
    
    # Update Chicken Roll items
    print("\nUpdating Chicken Roll images...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'chicken_roll_new.png' 
        WHERE name LIKE '%Chicken Roll%'
    """)
    print(f"  Updated {cursor.rowcount} Chicken Roll items")
    
    conn.commit()
    
    # Verify changes
    print("\n=== Verification ===")
    cursor.execute("""
        SELECT name, image_url 
        FROM menu 
        WHERE name LIKE '%Red Bull%' 
           OR name LIKE '%Veg Roll%' 
           OR name LIKE '%Egg Roll%' 
           OR name LIKE '%Paneer Roll%' 
           OR name LIKE '%Chicken Roll%'
        ORDER BY name
    """)
    results = cursor.fetchall()
    print(f"\nTotal items updated/verified: {len(results)}")
    
    # Show a sample of verified items
    print("\nSample of updated items:")
    for name, img in results[:10]:
        print(f"  {name}: {img}")
    
    conn.close()
    print("\n✓ Roll and Red Bull images updated successfully!")

if __name__ == '__main__':
    update_roll_images()
