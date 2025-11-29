import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), 'bmsbites.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def init_db():
    conn = sqlite3.connect(DB_PATH)
    with open(SCHEMA_PATH, 'r') as f:
        conn.executescript(f.read())
    
    cursor = conn.cursor()
    
    # Seed Admin Accounts
    admin_pass = generate_password_hash('admin123')
    cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                   ('admin', admin_pass, 'admin'))
    
    admin2_pass = generate_password_hash('admin456')
    cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                   ('canteen_admin', admin2_pass, 'admin'))
    
    # Seed Multiple Customer Accounts
    users = [
        ('rahul', 'user123', 'customer'),
        ('priya', 'pass123', 'customer'),
        ('amit', 'amit2024', 'customer'),
        ('sneha', 'sneha@123', 'customer'),
        ('karthik', 'karthik99', 'customer'),
        ('anjali', 'anjali456', 'customer'),
        ('rohan', 'rohan2025', 'customer'),
        ('divya', 'divya789', 'customer'),
    ]
    
    for username, password, role in users:
        hashed_pass = generate_password_hash(password)
        cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
                       (username, hashed_pass, role))

    # Seed Canteens
    canteens = [
        ('Vidhyarthi Khaana', 'Near Campus Book Mart', 'Largest canteen with variety of food', '8:00 AM', '8:00 PM', 1),
        ('Gowdas Canteen', 'Near BMS Mess', 'Fresh juices and beverages', '7:00 AM', '7:00 PM', 1),
        ('SIP & SNACK CAFE', 'Library', 'Fresh juices, shakes, and snacks', '8:00 AM', '8:00 PM', 1)
    ]
    cursor.executemany("INSERT INTO canteens (name, location, description, opening_time, closing_time, is_open) VALUES (?, ?, ?, ?, ?, ?)", canteens)

    # Seed Menu Items for Vidhyarthi Khaana (ID: 1)
    # Seed Menu Items for Vidhyarthi Khaana (ID: 1) - Complete Menu with 225 items
    vidhyarthi_khaana_items = [
        (1, 'Coffee/Tea', 'Coffee/Tea', 10.0, 'beverage', 'hot_coffee.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Idly (2)', 'Idly (2)', 30.0, 'veg', 'idly.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Vada (1)', 'Vada (1)', 20.0, 'veg', 'vada_single.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Idly (2) + Vada (1)', 'Idly (2) + Vada (1)', 52.0, 'veg', 'idly_vada_combo.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Idly (1) + Vada (1)', 'Idly (1) + Vada (1)', 40.0, 'veg', 'idly_vada_single.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Idly (1)', 'Idly (1)', 18.0, 'veg', 'idly.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Rava Idly', 'Rava Idly', 35.0, 'veg', 'rava_idly.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Karabath', 'Karabath', 25.0, 'veg', 'karabath.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Kesari Bath', 'Kesari Bath', 30.0, 'veg', 'kesari_bath.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Chow Chow Bath', 'Chow Chow Bath', 50.0, 'veg', 'rice_bath.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Poori', 'Poori', 35.0, 'veg', 'poori.jpg', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Curd Vada', 'Curd Vada', 35.0, 'veg', 'curd_vada.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Bajji / Pakoda', 'Bajji / Pakoda', 40.0, 'veg', 'bajji_pakoda.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Special Rice Bath', 'Special Rice Bath', 50.0, 'veg', 'rice_bath.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Rice Bath', 'Rice Bath', 40.0, 'veg', 'rice_bath.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Buns (1)', 'Buns (1)', 30.0, 'veg', 'buns_new.png', 'SOUTH INDIAN BREAKFAST'),
        (1, 'Masala Dosa', 'Masala Dosa', 50.0, 'veg', 'masala_dosa.png', 'Dosa Items'),
        (1, 'Set Dosa', 'Set Dosa', 40.0, 'veg', 'set_dosa.png', 'Dosa Items'),
        (1, 'Khali Dosa', 'Khali Dosa', 35.0, 'veg', 'khali_dosa.png', 'Dosa Items'),
        (1, 'Onion Dosa', 'Onion Dosa', 45.0, 'veg', 'onion_dosa.png', 'Dosa Items'),
        (1, 'Rava Dosa', 'Rava Dosa', 60.0, 'veg', 'rava_dosa.png', 'Dosa Items'),
        (1, 'Rava Onion Dosa', 'Rava Onion Dosa', 65.0, 'veg', 'rava_dosa.png', 'Dosa Items'),
        (1, 'Special Masala Dosa', 'Special Masala Dosa', 60.0, 'veg', 'masala_dosa.png', 'Dosa Items'),
        (1, 'Special Palak Dosa', 'Special Palak Dosa', 65.0, 'veg', 'palak_dosa.png', 'Dosa Items'),
        (1, 'Neer Dosa', 'Neer Dosa', 30.0, 'veg', 'neer_dosa.png', 'Dosa Items'),
        (1, 'Gobi Masala Dosa', 'Gobi Masala Dosa', 55.0, 'veg', 'masala_dosa.png', 'Dosa Items'),
        (1, 'Sweet Corn Dosa', 'Sweet Corn Dosa', 55.0, 'veg', 'masala_dosa.png', 'Dosa Items'),
        (1, 'Mysore Masala Dosa', 'Mysore Masala Dosa', 55.0, 'veg', 'mysore_masala_dosa.jpg', 'Dosa Items'),
        (1, 'Today’s Special Dosa', 'Today’s Special Dosa', 60.0, 'veg', 'masala_dosa.png', 'Dosa Items'),
        (1, 'Veg Mix Dosa', 'Veg Mix Dosa', 60.0, 'veg', 'masala_dosa.png', 'Dosa Items'),
        (1, 'Onion Masala Dosa', 'Onion Masala Dosa', 55.0, 'veg', 'onion_dosa.png', 'Dosa Items'),
        (1, 'Paper Masala Dosa', 'Paper Masala Dosa', 65.0, 'veg', 'paper_dosa.png', 'Dosa Items'),
        (1, 'Paper Plain Dosa', 'Paper Plain Dosa', 50.0, 'veg', 'paper_dosa.png', 'Dosa Items'),
        (1, 'Open Pudi Masala Dosa', 'Open Pudi Masala Dosa', 65.0, 'veg', 'open_pudi_masala.png', 'Dosa Items'),
        (1, 'North Indian Meals', 'North Indian Meals', 60.0, 'veg', 'north_indian_meal.png', 'North Indian Meals'),
        (1, 'South Indian Meals', 'South Indian Meals', 45.0, 'veg', 'meals_thali.png', 'North Indian Meals'),
        (1, 'Curd Rice', 'Curd Rice', 25.0, 'veg', 'curd_rice.png', 'North Indian Meals'),
        (1, 'Veg Palav', 'Veg Palav', 40.0, 'veg', 'veg_palao.png', 'North Indian Meals'),
        (1, 'Jeera Rice', 'Jeera Rice', 45.0, 'veg', 'jeera_rice.png', 'North Indian Meals'),
        (1, 'Poori (2)', 'Poori (2)', 25.0, 'veg', 'poori.jpg', 'North Indian Meals'),
        (1, 'Chapati (1)', 'Chapati (1)', 20.0, 'veg', 'chapathi.jpg', 'North Indian Meals'),
        (1, 'Chapati (2)', 'Chapati (2)', 40.0, 'veg', 'chapathi.jpg', 'North Indian Meals'),
        (1, 'Parota (1)', 'Parota (1)', 20.0, 'veg', 'parota.jpg', 'North Indian Meals'),
        (1, 'Parota (2)', 'Parota (2)', 40.0, 'veg', 'parota.jpg', 'North Indian Meals'),
        (1, 'Ghee Rice', 'Ghee Rice', 50.0, 'veg', 'jeera_rice.png', 'North Indian Meals'),
        (1, 'Kesari Bath / Halwa', 'Kesari Bath / Halwa', 35.0, 'veg', 'kesari_bath.png', 'North Indian Meals'),
        (1, 'Gulab Jamun (1)', 'Gulab Jamun (1)', 15.0, 'veg', 'gulab_jamun.png', 'North Indian Meals'),
        (1, 'Veg Rice Bath', 'Veg Rice Bath', 40.0, 'veg', 'rice_bath.png', 'North Indian Meals'),
        (1, 'Badam Milk / Horlicks / Boost', 'Badam Milk / Horlicks / Boost', 25.0, 'beverage', 'badam_milk.png', 'North Indian Meals'),
        (1, 'Special Meals Charges', 'Special Meals Charges', 5.0, 'veg', 'meals_thali.png', 'North Indian Meals'),
        (1, 'Veg Noodles', 'Veg Noodles', 65.0, 'veg', 'veg_noodles.png', 'Rice and Noodles'),
        (1, 'Veg Fried Rice', 'Veg Fried Rice', 65.0, 'veg', 'veg_fried_rice.png', 'Rice and Noodles'),
        (1, 'Gobi Manchurian', 'Gobi Manchurian', 70.0, 'veg', 'gobi_manchurian_new.png', 'Rice and Noodles'),
        (1, 'Jeera Rice', 'Jeera Rice', 60.0, 'veg', 'jeera_rice.png', 'Rice and Noodles'),
        (1, 'Egg Noodles (2 eggs)', 'Egg Noodles (2 eggs)', 75.0, 'non-veg', 'egg_noodles_new.png', 'Rice and Noodles'),
        (1, 'Egg Fried Rice (2 eggs)', 'Egg Fried Rice (2 eggs)', 75.0, 'non-veg', 'egg_fried_rice_new.png', 'Rice and Noodles'),
        (1, 'Schezwan Paneer Veg Noodles', 'Schezwan Paneer Veg Noodles', 80.0, 'veg', 'schezwan_paneer_noodles.png', 'Rice and Noodles'),
        (1, 'Schezwan Veg Noodles', 'Schezwan Veg Noodles', 70.0, 'veg', 'schezwan_noodles_new.png', 'Rice and Noodles'),
        (1, 'Schezwan Veg Fried Rice', 'Schezwan Veg Fried Rice', 70.0, 'veg', 'schezwan_rice.jpg', 'Rice and Noodles'),
        (1, 'Schezwan Egg Noodles (2 eggs)', 'Schezwan Egg Noodles (2 eggs)', 80.0, 'non-veg', 'egg_noodles_new.png', 'Rice and Noodles'),
        (1, 'Schezwan Egg Fried Rice (2 eggs)', 'Schezwan Egg Fried Rice (2 eggs)', 80.0, 'non-veg', 'egg_fried_rice_new.png', 'Rice and Noodles'),
        (1, 'Paneer Veg Noodles', 'Paneer Veg Noodles', 75.0, 'veg', 'veg_noodles.png', 'Rice and Noodles'),
        (1, 'Paneer Veg Fried Rice', 'Paneer Veg Fried Rice', 75.0, 'veg', 'veg_fried_rice.png', 'Rice and Noodles'),
        (1, 'Mushroom Veg Noodles', 'Mushroom Veg Noodles', 75.0, 'veg', 'veg_noodles.png', 'Rice and Noodles'),
        (1, 'Mushroom Veg Fried Rice', 'Mushroom Veg Fried Rice', 75.0, 'veg', 'veg_fried_rice.png', 'Rice and Noodles'),
        (1, 'Schezwan Paneer Egg Noodles', 'Schezwan Paneer Egg Noodles', 90.0, 'non-veg', 'schezwan_paneer_noodles.png', 'Rice and Noodles'),
        (1, 'Schezwan Paneer Egg Rice', 'Schezwan Paneer Egg Rice', 90.0, 'non-veg', 'egg_fried_rice_new.png', 'Rice and Noodles'),
        (1, 'Schezwan Mushroom', 'Schezwan Mushroom', 90.0, 'veg', 'mushroom_manchurian.jpg', 'Rice and Noodles'),
        (1, 'Egg Noodles', 'Egg Noodles', 90.0, 'non-veg', 'egg_noodles_new.png', 'Rice and Noodles'),
        (1, 'Schezwan Mushroom Egg Rice', 'Schezwan Mushroom Egg Rice', 90.0, 'non-veg', 'egg_fried_rice_new.png', 'Rice and Noodles'),
        (1, 'Triple Veg Fried Rice', 'Triple Veg Fried Rice', 75.0, 'veg', 'veg_fried_rice.png', 'Rice and Noodles'),
        (1, 'Triple Egg Fried Rice (2 eggs)', 'Triple Egg Fried Rice (2 eggs)', 85.0, 'non-veg', 'egg_fried_rice_new.png', 'Rice and Noodles'),
        (1, 'Gobi Noodles', 'Gobi Noodles', 75.0, 'veg', 'veg_noodles.png', 'Rice and Noodles'),
        (1, 'Gobi Rice', 'Gobi Rice', 75.0, 'veg', 'veg_fried_rice.png', 'Rice and Noodles'),
        (1, 'Roti Curry', 'Roti Curry', 50.0, 'veg', 'north_indian_meal.png', 'Rice and Noodles'),
        (1, 'Paneer Egg Noodles', 'Paneer Egg Noodles', 80.0, 'non-veg', 'egg_noodles_new.png', 'Rice and Noodles'),
        (1, 'Mushroom Egg Noodles', 'Mushroom Egg Noodles', 80.0, 'non-veg', 'egg_noodles_new.png', 'Rice and Noodles'),
        (1, 'Mushroom Egg Fried Rice', 'Mushroom Egg Fried Rice', 80.0, 'non-veg', 'egg_fried_rice_new.png', 'Rice and Noodles'),
        (1, 'Schezwan Mushroom Veg Noodles', 'Schezwan Mushroom Veg Noodles', 80.0, 'veg', 'schezwan_noodles_new.png', 'Rice and Noodles'),
        (1, 'Schezwan Mushroom Veg Rice', 'Schezwan Mushroom Veg Rice', 80.0, 'veg', 'schezwan_rice.jpg', 'Rice and Noodles'),
        (1, 'Mosambi Juice', 'Mosambi Juice', 40.0, 'beverage', 'mosambi_juice.png', 'FRESH JUICE'),
        (1, 'Watermelon Juice', 'Watermelon Juice', 30.0, 'beverage', 'watermelon_juice.png', 'FRESH JUICE'),
        (1, 'Pineapple Juice', 'Pineapple Juice', 45.0, 'beverage', 'pineapple_juice.png', 'FRESH JUICE'),
        (1, 'Orange Juice', 'Orange Juice', 45.0, 'beverage', 'orange_juice.png', 'FRESH JUICE'),
        (1, 'Grape Juice', 'Grape Juice', 40.0, 'beverage', 'grape_juice.png', 'FRESH JUICE'),
        (1, 'Karbooja / Musk Melon Juice', 'Karbooja / Musk Melon Juice', 45.0, 'beverage', 'muskmelon_juice.png', 'FRESH JUICE'),
        (1, 'Papaya Juice', 'Papaya Juice', 45.0, 'beverage', 'papaya_juice.png', 'FRESH JUICE'),
        (1, 'Lime Juice', 'Lime Juice', 20.0, 'beverage', 'lime_soda.png', 'FRESH JUICE'),
        (1, 'Mixed Fruit Juice / Solid', 'Mixed Fruit Juice / Solid', 50.0, 'beverage', 'mixed_fruit_juice.png', 'FRESH JUICE'),
        (1, 'Mosambi / Solid Orange Juice', 'Mosambi / Solid Orange Juice', 50.0, 'beverage', 'mosambi_juice.png', 'FRESH JUICE'),
        (1, 'Pista Badam', 'Pista Badam', 30.0, 'beverage', 'badam_milk.png', 'FRESH JUICE'),
        (1, 'Mango', 'Mango', 60.0, 'beverage', 'mango_juice.png', 'FRESH JUICE'),
        (1, 'Lychee', 'Lychee', 60.0, 'beverage', 'lychee_juice.png', 'FRESH JUICE'),
        (1, 'Kesar Pista', 'Kesar Pista', 38.0, 'beverage', 'badam_milk.png', 'FRESH JUICE'),
        (1, 'Vanilla Choco Chips', 'Vanilla Choco Chips', 38.0, 'beverage', 'milkshake.jpg', 'FRESH JUICE'),
        (1, 'Dairy Rich Delight Special', 'Dairy Rich Delight Special', 38.0, 'beverage', 'milkshake.jpg', 'FRESH JUICE'),


        (1, 'Omlet', 'Omlet', 35.0, 'non-veg', 'plain_omelette_new.png', 'Egg Omlet'),
        (1, 'Bread Omlet', 'Bread Omlet', 40.0, 'non-veg', 'bread_omelette_new.png', 'Egg Omlet'),
        (1, 'Cheese Omlet', 'Cheese Omlet', 45.0, 'non-veg', 'cheese_omelette.jpg', 'Egg Omlet'),
        (1, 'Bread Omlet with Cheese', 'Bread Omlet with Cheese', 50.0, 'non-veg', 'bread_omelette_new.png', 'Egg Omlet'),
        (1, 'Corn Omlet', 'Corn Omlet', 50.0, 'non-veg', 'corn_omelette_new.png', 'Egg Omlet'),
        (1, 'Corn Omlet with Cheese', 'Corn Omlet with Cheese', 55.0, 'non-veg', 'corn_omelette_new.png', 'Egg Omlet'),
        (1, 'Paneer Cheese Omlet', 'Paneer Cheese Omlet', 60.0, 'non-veg', 'paneer_omelette_new.png', 'Egg Omlet'),
        (1, 'Mushroom Omlet', 'Mushroom Omlet', 45.0, 'non-veg', 'mushroom_omelette_new.png', 'Egg Omlet'),
        (1, 'Mushroom Cheese Omlet', 'Mushroom Cheese Omlet', 50.0, 'non-veg', 'mushroom_omelette_new.png', 'Egg Omlet'),
        (1, 'Lime Cheese Omlet', 'Lime Cheese Omlet', 45.0, 'non-veg', 'lime_cheese_omelette_new.png', 'Egg Omlet'),
        (1, 'Egg Burji', 'Egg Burji', 40.0, 'non-veg', 'egg_burji_new.png', 'Egg + Bread Items'),
        (1, 'Bread Burji', 'Bread Burji', 40.0, 'veg', 'bread_burji_new.png', 'Egg + Bread Items'),
        (1, 'Bread Egg Burji', 'Bread Egg Burji', 50.0, 'non-veg', 'bread_burji_new.png', 'Egg + Bread Items'),
        (1, 'Bread Paneer Egg Burji', 'Bread Paneer Egg Burji', 55.0, 'non-veg', 'bread_burji_new.png', 'Egg + Bread Items'),
        (1, 'Masala Maggie', 'Masala Maggie', 45.0, 'veg', 'masala_maggi_new.png', 'Maggie – Masala'),
        (1, 'Corn Masala Maggie', 'Corn Masala Maggie', 50.0, 'veg', 'corn_masala_maggi_new.png', 'Maggie – Masala'),
        (1, 'Paneer Masala Maggie', 'Paneer Masala Maggie', 55.0, 'veg', 'paneer_masala_maggi_new.png', 'Maggie – Masala'),
        (1, 'Babycorn Masala Maggie', 'Babycorn Masala Maggie', 55.0, 'veg', 'babycorn_masala_maggi_new.png', 'Maggie – Masala'),
        (1, 'Potato Masala Maggie', 'Potato Masala Maggie', 50.0, 'veg', 'potato_masala_maggi_new.png', 'Maggie – Masala'),
        (1, 'Cheese Masala Maggie', 'Cheese Masala Maggie', 55.0, 'veg', 'masala_maggi_new.png', 'Maggie – Masala'),
        (1, 'Veg Roll', 'Veg Roll', 50.0, 'veg', 'veg_roll_new.png', 'Rolls'),
        (1, 'Paneer Roll', 'Paneer Roll', 60.0, 'veg', 'paneer_roll_new.png', 'Rolls'),
        (1, 'Paneer Cheese Roll', 'Paneer Cheese Roll', 65.0, 'veg', 'paneer_roll_new.png', 'Rolls'),
        (1, 'Mushroom Roll', 'Mushroom Roll', 55.0, 'veg', 'mushroom_roll_new.png', 'Rolls'),
        (1, 'Mushroom Cheese Roll', 'Mushroom Cheese Roll', 60.0, 'veg', 'mushroom_roll_new.png', 'Rolls'),
        (1, 'Babycorn Roll', 'Babycorn Roll', 55.0, 'veg', 'veg_roll_new.png', 'Rolls'),
        (1, 'Schezwan Roll', 'Schezwan Roll', 50.0, 'veg', 'veg_roll_new.png', 'Rolls'),
        (1, 'Paneer Schezwan Roll', 'Paneer Schezwan Roll', 60.0, 'veg', 'paneer_roll_new.png', 'Rolls'),
        (1, 'Veg Egg Roll', 'Veg Egg Roll', 50.0, 'non-veg', 'egg_roll_new.png', 'Rolls'),
        (1, 'Egg Cheese Roll', 'Egg Cheese Roll', 55.0, 'non-veg', 'egg_roll_new.png', 'Rolls'),
        (1, 'Vada Pav', 'Vada Pav', 25.0, 'veg', 'vada_pav_new.png', 'Rolls'),
        (1, 'Bread Jam', 'Bread Jam', 40.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Veg Burger', 'Veg Burger', 50.0, 'veg', 'burger.jpg', 'Sandwich'),
        (1, 'Veg Cheese Burger', 'Veg Cheese Burger', 60.0, 'veg', 'burger.jpg', 'Sandwich'),
        (1, 'Veg Sandwich', 'Veg Sandwich', 50.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Veg Grill Sandwich', 'Veg Grill Sandwich', 60.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Cheese Grill Sandwich', 'Cheese Grill Sandwich', 65.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Onion Cheese Grill', 'Onion Cheese Grill', 60.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Chilly Cheese Grill', 'Chilly Cheese Grill', 60.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Potato Cheese Grill', 'Potato Cheese Grill', 60.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Potato Onion Cheese Grill', 'Potato Onion Cheese Grill', 60.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Paneer Veg Grill', 'Paneer Veg Grill', 60.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Paneer Cheese Grill', 'Paneer Cheese Grill', 65.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Sweet Corn Sandwich', 'Sweet Corn Sandwich', 60.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Sweet Corn Cheese Sandwich', 'Sweet Corn Cheese Sandwich', 65.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Babycorn Sandwich', 'Babycorn Sandwich', 60.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Babycorn Cheese Sandwich', 'Babycorn Cheese Sandwich', 65.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Mushroom Cheese Sandwich', 'Mushroom Cheese Sandwich', 65.0, 'veg', 'sandwich.jpg', 'Sandwich'),
        (1, 'Plain Masala Sandwich', 'Plain Masala Sandwich', 50.0, 'veg', 'sandwich.jpg', 'Masala Sandwich'),
        (1, 'Egg Masala Sandwich (2 eggs)', 'Egg Masala Sandwich (2 eggs)', 60.0, 'non-veg', 'egg_burji.jpg', 'Masala Sandwich'),
        (1, 'Paneer Masala Sandwich', 'Paneer Masala Sandwich', 60.0, 'veg', 'sandwich.jpg', 'Masala Sandwich'),
        (1, 'Sweet Corn Masala Sandwich', 'Sweet Corn Masala Sandwich', 60.0, 'veg', 'sandwich.jpg', 'Masala Sandwich'),
        (1, 'Babycorn Masala Sandwich', 'Babycorn Masala Sandwich', 60.0, 'veg', 'sandwich.jpg', 'Masala Sandwich'),
        (1, 'Potato Masala Sandwich', 'Potato Masala Sandwich', 55.0, 'veg', 'sandwich.jpg', 'Masala Sandwich'),
        (1, 'Onion Masala Sandwich', 'Onion Masala Sandwich', 50.0, 'veg', 'sandwich.jpg', 'Masala Sandwich'),
        (1, 'Capsicum Masala Sandwich', 'Capsicum Masala Sandwich', 50.0, 'veg', 'sandwich.jpg', 'Masala Sandwich'),
        (1, 'Veg Maggie', 'Veg Maggie', 45.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Veg Fry Maggie', 'Veg Fry Maggie', 50.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Veg Maggie with Cheese', 'Veg Maggie with Cheese', 55.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Veg Fry Maggie with Cheese', 'Veg Fry Maggie with Cheese', 60.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Paneer Maggie', 'Paneer Maggie', 60.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Paneer Maggie with Cheese', 'Paneer Maggie with Cheese', 65.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Sweet Corn Maggie', 'Sweet Corn Maggie', 55.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Sweet Corn Maggie with Cheese', 'Sweet Corn Maggie with Cheese', 60.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Baby Corn Veg Maggie', 'Baby Corn Veg Maggie', 60.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Baby Corn Maggie with Cheese', 'Baby Corn Maggie with Cheese', 65.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Special Veg Fry Maggie', 'Special Veg Fry Maggie', 70.0, 'veg', 'maggie.jpg', 'Veg Maggie'),
        (1, 'Egg Fry Maggie', 'Egg Fry Maggie', 60.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Boiled Egg Maggie', 'Boiled Egg Maggie', 60.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Egg Fry Maggie with Cheese', 'Egg Fry Maggie with Cheese', 65.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Paneer Egg Fry Maggie', 'Paneer Egg Fry Maggie', 70.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Paneer Egg Fry Maggie with Cheese', 'Paneer Egg Fry Maggie with Cheese', 75.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Mushroom Egg Fry Maggie', 'Mushroom Egg Fry Maggie', 65.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Mushroom Egg Fry Maggie with Cheese', 'Mushroom Egg Fry Maggie with Cheese', 70.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Corn Egg Fry Maggie', 'Corn Egg Fry Maggie', 65.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Corn Egg Fry Maggie with Cheese', 'Corn Egg Fry Maggie with Cheese', 70.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Baby Corn Egg Fry Maggie', 'Baby Corn Egg Fry Maggie', 65.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Baby Corn Egg Fry Maggie with Cheese', 'Baby Corn Egg Fry Maggie with Cheese', 70.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
        (1, 'Special Egg Fry Maggie', 'Special Egg Fry Maggie', 80.0, 'non-veg', 'egg_burji.jpg', 'Egg Maggie'),
    ]

    # Seed Menu Items for Gowdas Canteen (ID: 2)
    gowdas_canteen_items = [
        # ENERGY ZONE
        (2, 'Red Bull Energy Drink', 'Red Bull Energy Drink', 150.0, 'beverage', 'redbull_new.png', 'ENERGY ZONE'),
        (2, 'Red Bull Sugar Free', 'Red Bull Sugar Free', 150.0, 'beverage', 'redbull_new.png', 'ENERGY ZONE'),
        (2, 'Red Bull Yellow Edition', 'Red Bull Yellow Edition', 175.0, 'beverage', 'redbull_new.png', 'ENERGY ZONE'),
        
        # ROLLS
        (2, 'Veg Roll', 'Veg Roll', 45.0, 'veg', 'veg_roll_new.png', 'ROLLS'),
        (2, 'Veg Roll with Cheese', 'Veg Roll with Cheese', 65.0, 'veg', 'veg_roll_new.png', 'ROLLS'),
        (2, 'Egg Roll', 'Egg Roll', 55.0, 'non-veg', 'egg_roll_new.png', 'ROLLS'),
        (2, 'Egg Roll with Cheese', 'Egg Roll with Cheese', 75.0, 'non-veg', 'egg_roll_new.png', 'ROLLS'),
        (2, 'Chicken Roll', 'Chicken Roll', 75.0, 'non-veg', 'chicken_roll_new.png', 'ROLLS'),
        (2, 'Chicken Roll with Cheese', 'Chicken Roll with Cheese', 95.0, 'non-veg', 'chicken_roll_new.png', 'ROLLS'),
        (2, 'Paneer Roll', 'Paneer Roll', 65.0, 'veg', 'paneer_roll_new.png', 'ROLLS'),
        (2, 'Paneer Roll with Cheese', 'Paneer Roll with Cheese', 87.0, 'veg', 'paneer_roll_new.png', 'ROLLS'),
        (2, 'Mushroom Roll', 'Mushroom Roll', 75.0, 'veg', 'mushroom_roll_new.png', 'ROLLS'),
        (2, 'Mushroom Roll with Cheese', 'Mushroom Roll with Cheese', 95.0, 'veg', 'mushroom_roll_new.png', 'ROLLS'),
        
        # MASALA MAGGI
        (2, 'Masala Cooking Maggi', 'Masala Cooking Maggi', 35.0, 'veg', 'masala_maggi_new.png', 'MASALA MAGGI'),
        (2, 'Masala Cooking Maggi Cheese', 'Masala Cooking Maggi with Cheese', 50.0, 'veg', 'masala_maggi_new.png', 'MASALA MAGGI'),
        (2, 'Egg Masala Maggi', 'Egg Masala Maggi', 50.0, 'non-veg', 'masala_maggi_new.png', 'MASALA MAGGI'),
        (2, 'Egg Masala Maggi Cheese', 'Egg Masala Maggi with Cheese', 65.0, 'non-veg', 'masala_maggi_new.png', 'MASALA MAGGI'),
        (2, 'Paneer Masala Maggi', 'Paneer Masala Maggi', 65.0, 'veg', 'paneer_masala_maggi_new.png', 'MASALA MAGGI'),
        (2, 'Paneer Masala Maggi Cheese', 'Paneer Masala Maggi with Cheese', 75.0, 'veg', 'paneer_masala_maggi_new.png', 'MASALA MAGGI'),
        (2, 'Chicken Masala Maggi', 'Chicken Masala Maggi', 75.0, 'non-veg', 'masala_maggi_new.png', 'MASALA MAGGI'),
        (2, 'Chicken Masala Maggi Cheese', 'Chicken Masala Maggi with Cheese', 97.0, 'non-veg', 'masala_maggi_new.png', 'MASALA MAGGI'),
        
        # WAI WAI MAGGI
        (2, 'Veg Wai Wai Maggi Masala', 'Veg Wai Wai Maggi Masala', 40.0, 'veg', 'masala_maggi_new.png', 'WAI WAI MAGGI'),
        (2, 'Veg Wai Wai Maggi Masala Cheese', 'Veg Wai Wai Maggi Masala with Cheese', 55.0, 'veg', 'masala_maggi_new.png', 'WAI WAI MAGGI'),
        (2, 'Chicken Wai Wai Maggi', 'Chicken Wai Wai Maggi', 50.0, 'non-veg', 'masala_maggi_new.png', 'WAI WAI MAGGI'),
        (2, 'Chicken Wai Wai Maggi with Cheese', 'Chicken Wai Wai Maggi with Cheese', 65.0, 'non-veg', 'masala_maggi_new.png', 'WAI WAI MAGGI'),
        
        # PASTA / MAGGI PASTA
        (2, 'Tomato Pasta', 'Tomato Pasta', 58.0, 'veg', 'maggie.jpg', 'PASTA / MAGGI PASTA'),
        (2, 'Masala Pasta', 'Masala Pasta', 58.0, 'veg', 'maggie.jpg', 'PASTA / MAGGI PASTA'),
        (2, 'Mushroom Pasta', 'Mushroom Pasta', 58.0, 'veg', 'maggie.jpg', 'PASTA / MAGGI PASTA'),
        (2, 'Cheese Pasta', 'Cheese Pasta', 78.0, 'veg', 'maggie.jpg', 'PASTA / MAGGI PASTA'),
        (2, 'Extra Cheese', 'Extra Cheese', 20.0, 'veg', 'maggie.jpg', 'PASTA / MAGGI PASTA'),
        
        # HOT DOGS
        (2, 'Veg Hot Dog', 'Veg Hot Dog', 35.0, 'veg', 'sandwich.jpg', 'HOT DOGS'),
        (2, 'Veg Hot Dog Cheese', 'Veg Hot Dog with Cheese', 45.0, 'veg', 'sandwich.jpg', 'HOT DOGS'),
        (2, 'Veg Hot Dog Cheese + Chips', 'Veg Hot Dog with Cheese and Chips', 65.0, 'veg', 'sandwich.jpg', 'HOT DOGS'),
        (2, 'Veg Paneer Hot Dog', 'Veg Paneer Hot Dog', 55.0, 'veg', 'sandwich.jpg', 'HOT DOGS'),
        (2, 'Veg Paneer Hot Dog Cheese', 'Veg Paneer Hot Dog with Cheese', 65.0, 'veg', 'sandwich.jpg', 'HOT DOGS'),
        (2, 'Veg Hot Dog Omelette', 'Veg Hot Dog with Omelette', 55.0, 'non-veg', 'bread_omelette_new.png', 'HOT DOGS'),
        (2, 'Chicken Hot Dog', 'Chicken Hot Dog', 65.0, 'non-veg', 'sandwich.jpg', 'HOT DOGS'),
        (2, 'Chicken Hot Dog Cheese', 'Chicken Hot Dog with Cheese', 75.0, 'non-veg', 'sandwich.jpg', 'HOT DOGS'),
        (2, 'Chicken Hot Dog Cheese + Chips', 'Chicken Hot Dog with Cheese and Chips', 87.0, 'non-veg', 'sandwich.jpg', 'HOT DOGS'),
        
        # EGG ITEMS
        (2, 'Bun Omelette Plain', 'Bun Omelette Plain', 35.0, 'non-veg', 'bread_omelette_new.png', 'EGG ITEMS'),
        (2, 'Bun Omelette Cheese & Chips', 'Bun Omelette with Cheese and Chips', 65.0, 'non-veg', 'bread_omelette_new.png', 'EGG ITEMS'),
        (2, 'Bread Omelette Plain', 'Bread Omelette Plain', 25.0, 'non-veg', 'bread_omelette_new.png', 'EGG ITEMS'),
        (2, 'Single Omelette', 'Single Omelette', 20.0, 'non-veg', 'plain_omelette_new.png', 'EGG ITEMS'),
        (2, 'Double Omelette', 'Double Omelette', 25.0, 'non-veg', 'plain_omelette_new.png', 'EGG ITEMS'),
        (2, 'Egg Puff', 'Egg Puff', 25.0, 'non-veg', 'egg_burji.jpg', 'EGG ITEMS'),
        (2, 'Egg Puff Cheese', 'Egg Puff with Cheese', 35.0, 'non-veg', 'egg_burji.jpg', 'EGG ITEMS'),
        (2, 'Bun Butter Egg Puff', 'Bun Butter Egg Puff', 45.0, 'non-veg', 'egg_burji.jpg', 'EGG ITEMS'),
        (2, 'Bun Butter Egg Puff Cheese', 'Bun Butter Egg Puff with Cheese', 55.0, 'non-veg', 'egg_burji.jpg', 'EGG ITEMS'),
        
        # BURGER
        (2, 'Veg Burger Plain', 'Veg Burger Plain', 35.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Veg Burger Cheese', 'Veg Burger with Cheese', 50.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Veg Burger Cheese + Chips', 'Veg Burger with Cheese and Chips', 50.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Paneer Burger', 'Paneer Burger', 50.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Paneer Burger Cheese', 'Paneer Burger with Cheese', 65.0, 'veg', 'burger.jpg', 'BURGER'),
        (2, 'Chicken Burger', 'Chicken Burger', 75.0, 'non-veg', 'burger.jpg', 'BURGER'),
        (2, 'Chicken Burger with Cheese', 'Chicken Burger with Cheese', 87.0, 'non-veg', 'burger.jpg', 'BURGER'),
        
        # MAGGI SPECIAL
        (2, 'Veg Fried Maggi', 'Veg Fried Maggi', 55.0, 'veg', 'masala_maggi_new.png', 'MAGGI SPECIAL'),
        (2, 'Veg Fried Maggi Cheese', 'Veg Fried Maggi with Cheese', 65.0, 'veg', 'masala_maggi_new.png', 'MAGGI SPECIAL'),
        (2, 'Chicken Fried Maggi', 'Chicken Fried Maggi', 75.0, 'non-veg', 'masala_maggi_new.png', 'MAGGI SPECIAL'),
        (2, 'Chicken Fried Maggi Cheese', 'Chicken Fried Maggi with Cheese', 87.0, 'non-veg', 'masala_maggi_new.png', 'MAGGI SPECIAL'),
        (2, 'Egg Fried Maggi', 'Egg Fried Maggi', 55.0, 'non-veg', 'masala_maggi_new.png', 'MAGGI SPECIAL'),
        (2, 'Egg Fried Maggi Cheese', 'Egg Fried Maggi with Cheese', 65.0, 'non-veg', 'masala_maggi_new.png', 'MAGGI SPECIAL'),
        
        # SAMOSA
        (2, 'Samosa', 'Samosa', 20.0, 'veg', 'samosa_chat.jpg', 'SAMOSA'),
        (2, 'Samosa Chat Masala', 'Samosa Chat Masala', 40.0, 'veg', 'samosa_chat.jpg', 'SAMOSA'),
        (2, 'Bun Samosa Plain', 'Bun Samosa Plain', 30.0, 'veg', 'samosa_chat.jpg', 'SAMOSA'),
        (2, 'Bun Samosa Cheese', 'Bun Samosa with Cheese', 45.0, 'veg', 'samosa_chat.jpg', 'SAMOSA'),
        
        # PUFFS
        (2, 'Veg Puff', 'Veg Puff', 25.0, 'veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Veg Puff Cheese', 'Veg Puff with Cheese', 35.0, 'veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Bun Veg Puff', 'Bun Veg Puff', 45.0, 'veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Bun Veg Puff Cheese', 'Bun Veg Puff with Cheese', 55.0, 'veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Paneer Puff', 'Paneer Puff', 50.0, 'veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Paneer Puff Cheese', 'Paneer Puff with Cheese', 60.0, 'veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Paneer Puff Cheese + Chips', 'Paneer Puff with Cheese and Chips', 75.0, 'veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Chicken Puff', 'Chicken Puff', 50.0, 'non-veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Chicken Puff Cheese', 'Chicken Puff with Cheese', 60.0, 'non-veg', 'bajji_pakoda.png', 'PUFFS'),
        (2, 'Chicken Puff Cheese + Chips', 'Chicken Puff with Cheese and Chips', 80.0, 'non-veg', 'bajji_pakoda.png', 'PUFFS'),
        
        # MOMOS
        (2, 'Veg Momos', 'Veg Momos', 65.0, 'veg', 'bajji_pakoda.png', 'MOMOS'),
        (2, 'Chicken Momos', 'Chicken Momos', 75.0, 'non-veg', 'bajji_pakoda.png', 'MOMOS'),
        
        # BUN SECTION
        (2, 'Bun Butter Jam', 'Bun Butter Jam', 25.0, 'veg', 'buns_new.png', 'BUN SECTION'),
        (2, 'Bun Butter Jam Bread Toast', 'Bun Butter Jam Bread Toast', 30.0, 'veg', 'buns_new.png', 'BUN SECTION'),
        (2, 'Bun Masala', 'Bun Masala', 35.0, 'veg', 'buns_new.png', 'BUN SECTION'),
        (2, 'Bun Masala Cheese', 'Bun Masala with Cheese', 45.0, 'veg', 'buns_new.png', 'BUN SECTION'),
        
        # SOFT DRINKS & BEVERAGES
        (2, 'Coca Cola', 'Coca Cola', 20.0, 'beverage', 'coke_new.png', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Thumbs Up', 'Thumbs Up', 20.0, 'beverage', 'coke_new.png', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Mountain Dew', 'Mountain Dew', 20.0, 'beverage', 'coke_new.png', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Sprite', 'Sprite', 20.0, 'beverage', 'coke_new.png', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Paper Boat', 'Paper Boat', 25.0, 'beverage', 'juice.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Tropical Juice / Fruit Mix', 'Tropical Juice / Fruit Mix', 25.0, 'beverage', 'juice.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Fresh Juices', 'Fresh Juices', 40.0, 'beverage', 'juice.jpg', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Lime Juice', 'Lime Juice', 20.0, 'beverage', 'lime_soda.png', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Grape Juice', 'Grape Juice', 20.0, 'beverage', 'grape_juice.png', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Hot Coffee', 'Hot Coffee', 20.0, 'beverage', 'hot_coffee.png', 'SOFT DRINKS & BEVERAGES'),
        (2, 'Tea / Lemon Tea', 'Tea / Lemon Tea', 15.0, 'beverage', 'masala_tea.png', 'SOFT DRINKS & BEVERAGES'),
    ]

    # Seed Menu Items for SIP & SNACK CAFE (ID: 3)
    sip_snack_cafe_items = [
        # FRESH JUICE
        (3, 'Mosambi', 'Fresh Mosambi Juice', 40.0, 'beverage', 'mosambi_juice.png', 'FRESH JUICE'),
        (3, 'Orange', 'Fresh Orange Juice', 50.0, 'beverage', 'orange_juice.png', 'FRESH JUICE'),
        (3, 'Pineapple', 'Fresh Pineapple Juice', 40.0, 'beverage', 'pineapple_juice.png', 'FRESH JUICE'),
        (3, 'Watermelon', 'Fresh Watermelon Juice', 40.0, 'beverage', 'watermelon_juice.png', 'FRESH JUICE'),
        (3, 'Muskmelon', 'Fresh Muskmelon Juice', 40.0, 'beverage', 'juice.jpg', 'FRESH JUICE'),
        (3, 'Anar', 'Fresh Pomegranate Juice', 50.0, 'beverage', 'juice.jpg', 'FRESH JUICE'),
        (3, 'Grape', 'Fresh Grape Juice', 40.0, 'beverage', 'grape_juice.png', 'FRESH JUICE'),
        (3, 'Mango', 'Fresh Mango Juice', 50.0, 'beverage', 'juice.jpg', 'FRESH JUICE'),
        (3, 'Apple', 'Fresh Apple Juice', 50.0, 'beverage', 'juice.jpg', 'FRESH JUICE'),
        (3, 'Lime', 'Fresh Lime Juice', 20.0, 'beverage', 'lime_soda.png', 'FRESH JUICE'),
        (3, 'Ginger Lime', 'Ginger Lime Juice', 30.0, 'beverage', 'lime_soda.png', 'FRESH JUICE'),
        (3, 'Kiwi Lime', 'Kiwi Lime Juice', 40.0, 'beverage', 'juice.jpg', 'FRESH JUICE'),
        (3, 'Strawberry Lime', 'Strawberry Lime Juice', 40.0, 'beverage', 'juice.jpg', 'FRESH JUICE'),
        (3, 'Blue Lime', 'Blue Lime Juice', 40.0, 'beverage', 'juice.jpg', 'FRESH JUICE'),
        (3, 'Watermelon Mojito', 'Watermelon Mojito', 50.0, 'beverage', 'watermelon_juice.png', 'FRESH JUICE'),
        (3, 'Pineapple Mojito', 'Pineapple Mojito', 50.0, 'beverage', 'pineapple_juice.png', 'FRESH JUICE'),
        
        # SODA
        (3, 'Lime Soda Salt', 'Lime Soda with Salt', 30.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Lime Soda Sweet', 'Lime Soda Sweet', 30.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Grape Soda', 'Grape Soda', 40.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Passion Fruit Soda', 'Passion Fruit Soda', 50.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Strawberry Soda', 'Strawberry Soda', 50.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Sweet Lime Soda', 'Sweet Lime Soda', 30.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Blue Lime Soda', 'Blue Lime Soda', 50.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Nannari Sharbat', 'Nannari Sharbat', 40.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Masala Soda', 'Masala Soda', 40.0, 'beverage', 'lime_soda.png', 'SODA'),
        (3, 'Jal Jeera Soda', 'Jal Jeera Soda', 40.0, 'beverage', 'lime_soda.png', 'SODA'),
        
        # SHAKES
        (3, 'Rose Milk', 'Rose Milk', 50.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Apple Shake', 'Apple Shake', 70.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Banana Shake', 'Banana Shake', 60.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Chikku Shake', 'Chikku Shake', 60.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Papaya Shake', 'Papaya Shake', 50.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Muskmelon Shake', 'Muskmelon Shake', 60.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Anar Shake', 'Anar Shake', 70.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Mixed Fruit Shake', 'Mixed Fruit Shake', 60.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Avocado Shake', 'Avocado Shake', 80.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Strawberry Shake', 'Strawberry Shake', 80.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Oreo Shake', 'Oreo Shake', 60.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'SP Oreo', 'SP Oreo', 70.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Skinny Oreo', 'Skinny Oreo', 60.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Nuv Shake', 'Nuv Shake', 60.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Litchi Shake', 'Litchi Shake', 60.0, 'beverage', 'milkshake.jpg', 'SHAKES'),
        (3, 'Cold Horlicks', 'Cold Horlicks', 60.0, 'beverage', 'badam_milk.png', 'SHAKES'),
        (3, 'Cold Boost', 'Cold Boost', 60.0, 'beverage', 'badam_milk.png', 'SHAKES'),
        (3, 'Cold Coffee', 'Cold Coffee', 60.0, 'beverage', 'cold_coffee.png', 'SHAKES'),
        (3, 'Cold Coffee Ice Cream', 'Cold Coffee with Ice Cream', 70.0, 'beverage', 'cold_coffee.png', 'SHAKES'),
        (3, 'Cold Boost Ice Cream', 'Cold Boost with Ice Cream', 80.0, 'beverage', 'badam_milk.png', 'SHAKES'),
        (3, 'Cold Horlicks Ice Cream', 'Cold Horlicks with Ice Cream', 80.0, 'beverage', 'badam_milk.png', 'SHAKES'),
        
        # SPECIAL SHAKES
        (3, 'Mango Banana', 'Mango Banana Shake', 90.0, 'beverage', 'milkshake.jpg', 'SPECIAL SHAKES'),
        (3, 'Papaya Mango', 'Papaya Mango Shake', 90.0, 'beverage', 'milkshake.jpg', 'SPECIAL SHAKES'),
        (3, 'Mango', 'Mango Shake', 60.0, 'beverage', 'milkshake.jpg', 'SPECIAL SHAKES'),
        (3, 'Strawberry', 'Strawberry Shake', 90.0, 'beverage', 'milkshake.jpg', 'SPECIAL SHAKES'),
        (3, 'Aval Milk', 'Aval Milk', 60.0, 'beverage', 'badam_milk.png', 'SPECIAL SHAKES'),
        (3, 'Brownie Shake', 'Brownie Shake', 60.0, 'beverage', 'milkshake.jpg', 'SPECIAL SHAKES'),
        
        # SIP & SNACK SP SHAKE
        (3, 'Passion Mango', 'Passion Mango Shake', 90.0, 'beverage', 'milkshake.jpg', 'SIP & SNACK SP SHAKE'),
        (3, 'Jackfruit Milkshake', 'Jackfruit Milkshake', 70.0, 'beverage', 'milkshake.jpg', 'SIP & SNACK SP SHAKE'),
        (3, 'Fig with Strawberry', 'Fig with Strawberry Shake', 70.0, 'beverage', 'milkshake.jpg', 'SIP & SNACK SP SHAKE'),
        (3, 'Papaya with Mango', 'Papaya with Mango Shake', 90.0, 'beverage', 'milkshake.jpg', 'SIP & SNACK SP SHAKE'),
        (3, 'Aval Milk with Ice Cream', 'Aval Milk with Ice Cream', 80.0, 'beverage', 'milkshake.jpg', 'SIP & SNACK SP SHAKE'),
        
        # ICE CREAM
        (3, 'Vanilla', 'Vanilla Ice Cream', 25.0, 'beverage', 'icecream.jpg', 'ICE CREAM'),
        (3, 'Chocolate', 'Chocolate Ice Cream', 30.0, 'beverage', 'icecream.jpg', 'ICE CREAM'),
        (3, 'Strawberry', 'Strawberry Ice Cream', 30.0, 'beverage', 'icecream.jpg', 'ICE CREAM'),
        (3, 'Butterscotch', 'Butterscotch Ice Cream', 30.0, 'beverage', 'icecream.jpg', 'ICE CREAM'),
        
        # ROLLS
        (3, 'Veg Roll', 'Veg Roll', 50.0, 'veg', 'veg_roll_new.png', 'ROLLS'),
        (3, 'Veg Special Roll', 'Veg Special Roll', 60.0, 'veg', 'veg_roll_new.png', 'ROLLS'),
        (3, 'Paneer Roll', 'Paneer Roll', 50.0, 'veg', 'paneer_roll_new.png', 'ROLLS'),
        (3, 'Paneer Cheese Roll', 'Paneer Cheese Roll', 60.0, 'veg', 'paneer_roll_new.png', 'ROLLS'),
        (3, 'Falafel Roll', 'Falafel Roll', 50.0, 'veg', 'veg_roll_new.png', 'ROLLS'),
        (3, 'Mushroom Roll', 'Mushroom Roll', 50.0, 'veg', 'mushroom_roll_new.png', 'ROLLS'),
        (3, 'Crunchy Bite Roll', 'Crunchy Bite Roll', 50.0, 'veg', 'veg_roll_new.png', 'ROLLS'),
        (3, 'Veg Corn Roll', 'Veg Corn Roll', 60.0, 'veg', 'veg_roll_new.png', 'ROLLS'),
        
        # BURGERS
        (3, 'Veg Burger', 'Veg Burger', 50.0, 'veg', 'burger.jpg', 'BURGERS'),
        (3, 'Veg Cheese Burger', 'Veg Cheese Burger', 60.0, 'veg', 'burger.jpg', 'BURGERS'),
        (3, 'Veg Special Burger', 'Veg Special Burger', 70.0, 'veg', 'burger.jpg', 'BURGERS'),
        (3, 'Paneer Burger', 'Paneer Burger', 50.0, 'veg', 'burger.jpg', 'BURGERS'),
        (3, 'Paneer Cheese Burger', 'Paneer Cheese Burger', 60.0, 'veg', 'burger.jpg', 'BURGERS'),
        (3, 'Zinger Burger', 'Zinger Burger', 60.0, 'veg', 'burger.jpg', 'BURGERS'),
        (3, 'Zinger Mushroom Burger', 'Zinger Mushroom Burger', 80.0, 'veg', 'burger.jpg', 'BURGERS'),
        (3, 'Double Beamer', 'Double Beamer Burger', 80.0, 'veg', 'burger.jpg', 'BURGERS'),
        
        # SNACKS
        (3, 'Veg Cutlet', 'Veg Cutlet', 30.0, 'veg', 'bajji_pakoda.png', 'SNACKS'),
        (3, 'Potato Twisters', 'Potato Twisters', 60.0, 'veg', 'bajji_pakoda.png', 'SNACKS'),
        (3, 'Falafel Nuggets', 'Falafel Nuggets', 50.0, 'veg', 'bajji_pakoda.png', 'SNACKS'),
        (3, 'Veg Nuggets Plate', 'Veg Nuggets Plate', 50.0, 'veg', 'bajji_pakoda.png', 'SNACKS'),
        (3, 'Peri Peri Fries', 'Peri Peri Fries', 50.0, 'veg', 'bajji_pakoda.png', 'SNACKS'),
        (3, 'French Fries', 'French Fries', 50.0, 'veg', 'bajji_pakoda.png', 'SNACKS'),
        (3, 'Vada Pav', 'Vada Pav', 30.0, 'veg', 'vada_pav_new.png', 'SNACKS'),
        
        # SANDWICH
        (3, 'Veg Sandwich', 'Veg Sandwich', 40.0, 'veg', 'sandwich.jpg', 'SANDWICH'),
        (3, 'Veg Club', 'Veg Club Sandwich', 50.0, 'veg', 'sandwich.jpg', 'SANDWICH'),
        (3, 'Veg Cheese Sandwich', 'Veg Cheese Sandwich', 50.0, 'veg', 'sandwich.jpg', 'SANDWICH'),
        (3, 'Veg Mayo Sandwich', 'Veg Mayo Sandwich', 50.0, 'veg', 'sandwich.jpg', 'SANDWICH'),
        (3, 'Special Club Sandwich', 'Special Club Sandwich', 70.0, 'veg', 'sandwich.jpg', 'SANDWICH'),
        (3, 'Falafel Sandwich', 'Falafel Sandwich', 50.0, 'veg', 'sandwich.jpg', 'SANDWICH'),
        (3, 'Crunchy Cheese Toast', 'Crunchy Cheese Toast', 60.0, 'veg', 'sandwich.jpg', 'SANDWICH'),
        
        # TEA & COFFEE ITEMS
        (3, 'Tea', 'Tea', 15.0, 'beverage', 'masala_tea.png', 'TEA & COFFEE ITEMS'),
        (3, 'Ginger Tea', 'Ginger Tea', 20.0, 'beverage', 'masala_tea.png', 'TEA & COFFEE ITEMS'),
        (3, 'Coffee', 'Coffee', 20.0, 'beverage', 'hot_coffee.png', 'TEA & COFFEE ITEMS'),
        (3, 'Chukku Coffee', 'Chukku Coffee', 20.0, 'beverage', 'hot_coffee.png', 'TEA & COFFEE ITEMS'),
        (3, 'Lime Tea', 'Lime Tea', 20.0, 'beverage', 'masala_tea.png', 'TEA & COFFEE ITEMS'),
        (3, 'Black Tea', 'Black Tea', 10.0, 'beverage', 'masala_tea.png', 'TEA & COFFEE ITEMS'),
        (3, 'Black Ginger Tea', 'Black Ginger Tea', 20.0, 'beverage', 'masala_tea.png', 'TEA & COFFEE ITEMS'),
        (3, 'Horlicks', 'Horlicks', 20.0, 'beverage', 'badam_milk.png', 'TEA & COFFEE ITEMS'),
        (3, 'Boost', 'Boost', 20.0, 'beverage', 'badam_milk.png', 'TEA & COFFEE ITEMS'),
        
        # MAGGI
        (3, 'Veg Maggi', 'Veg Maggi', 40.0, 'veg', 'masala_maggi_new.png', 'MAGGI'),
        (3, 'Paneer Maggi', 'Paneer Maggi', 60.0, 'veg', 'paneer_masala_maggi_new.png', 'MAGGI'),
        (3, 'Plain Maggi', 'Plain Maggi', 30.0, 'veg', 'masala_maggi_new.png', 'MAGGI'),
        (3, 'Cheese Maggi', 'Cheese Maggi', 60.0, 'veg', 'masala_maggi_new.png', 'MAGGI'),
        (3, 'Corn Maggi', 'Corn Maggi', 50.0, 'veg', 'corn_masala_maggi_new.png', 'MAGGI'),
    ]

    all_items = vidhyarthi_khaana_items + gowdas_canteen_items + sip_snack_cafe_items
    cursor.executemany("INSERT INTO menu (canteen_id, name, description, price, category, image_url, category_section) VALUES (?, ?, ?, ?, ?, ?, ?)", all_items)

    conn.commit()
    conn.close()
    print("Database initialized and seeded successfully.")
    print("✓ 10 Users created (2 admins, 8 customers)")
    print("✓ 3 Canteens created")
    print("✓ Menu items distributed across canteens")

if __name__ == '__main__':
    init_db()
