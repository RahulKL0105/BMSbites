import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database/bmsbites.db')

def update_vada_images():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Change Vada (1) back to vada.png (original)
    print("Updating Vada (1) image back to original...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'vada.png' 
        WHERE name = 'Vada (1)'
    """)
    print(f"  Updated {cursor.rowcount} items")
    
    # Update Idly (1) + Vada (1) to use the new uploaded image
    print("\nUpdating Idly (1) + Vada (1) image...")
    cursor.execute("""
        UPDATE menu 
        SET image_url = 'idly_vada_single.png' 
        WHERE name = 'Idly (1) + Vada (1)'
    """)
    print(f"  Updated {cursor.rowcount} items")
    
    conn.commit()
    
    # Verify changes
    print("\n=== Verification ===")
    cursor.execute("""
        SELECT name, image_url 
        FROM menu 
        WHERE name IN ('Vada (1)', 'Idly (1) + Vada (1)', 'Idly (2) + Vada (1)')
        ORDER BY name
    """)
    results = cursor.fetchall()
    for name, img in results:
        print(f"  {name}: {img}")
    
    conn.close()
    print("\n✓ Vada images updated successfully!")

if __name__ == '__main__':
    update_vada_images()
