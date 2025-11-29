import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/bmsbites.db')

def update_breakfast_images():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Update Buns (1)
    print("Updating Buns (1) image...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'buns_new.png' 
        WHERE name = 'Buns (1)'
    """)
    print(f"  Updated {cursor.rowcount} items")
    
    # Update Bajji / Pakoda
    print("\nUpdating Bajji / Pakoda image...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'bajji_pakoda.png' 
        WHERE name = 'Bajji / Pakoda'
    """)
    print(f"  Updated {cursor.rowcount} items")
    
    # Update Curd Vada
    print("\nUpdating Curd Vada image...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'curd_vada.png' 
        WHERE name = 'Curd Vada'
    """)
    print(f"  Updated {cursor.rowcount} items")
    
    conn.commit()
    
    # Verify changes
    print("\n=== Verification ===")
    cursor.execute("""
        SELECT name, image_url 
        FROM menu 
        WHERE name IN ('Buns (1)', 'Bajji / Pakoda', 'Curd Vada')
        ORDER BY name
    """)
    results = cursor.fetchall()
    print(f"\nUpdated {len(results)} items:")
    for name, img in results:
        print(f"  {name}: {img}")
    
    conn.close()
    print("\n✓ Breakfast item images updated successfully!")

if __name__ == '__main__':
    update_breakfast_images()
