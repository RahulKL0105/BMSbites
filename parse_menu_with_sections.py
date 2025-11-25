#!/usr/bin/env python3
# Assign category sections to all menu items based on the original document structure

import re

# Read the menu file
with open('VIDHYARTHI_KHANA_menu.txt', 'r') as f:
    lines = f.readlines()

menu_items = []
current_section = ''
current_subsection = ''

for line in lines:
    line = line.strip()
    
    # Skip empty lines and headers
    if not line or line.startswith('VIDHYARTHI') or line.startswith('BMS College') or line.startswith('South Indian /'):
        continue
    
    # Track main section headers (all caps or specific patterns)
    if line.isupper() or line.startswith('(Board'):
        current_section = line
        current_subsection = ''  # Reset subsection
        continue
    
    # Track subsection headers (title case, not all caps, no bullet)
    if not line.startswith('•') and not line.startswith('\t•') and line[0].isupper() and not line.isupper():
        # This is likely a subsection
        current_subsection = line
        continue
    
    # Parse menu items (format: • Item Name – Price)
    if '•' in line or '\t•\t' in line:
        # Extract item name and price
        match = re.search(r'•\s*(.+?)\s*[–-]\s*(\d+)', line)
        if match:
            item_name = match.group(1).strip()
            price = float(match.group(2))
            
            # Determine category based on item name and section
            category = 'veg'  # default
            
            # Check for beverages
            if any(word in item_name.lower() for word in ['juice', 'shake', 'coffee', 'tea', 'milk', 'ice cream', 'cone']):
                category = 'beverage'
            elif any(word in current_section.upper() for word in ['JUICE', 'MILK SHAKE', 'ICE CREAM']):
                category = 'beverage'
            # Check for non-veg items
            elif any(word in item_name.lower() for word in ['egg', 'omlet', 'omelette', 'burji']):
                category = 'non-veg'
            elif 'EGG' in current_section.upper() or 'OMLET' in current_section.upper():
                category = 'non-veg'
            
            # Fix categories for specific veg items
            veg_keywords = ['Veg Roll', 'Paneer Roll', 'Paneer Cheese Roll', 'Mushroom Roll', 'Mushroom Cheese Roll', 
                            'Babycorn Roll', 'Schezwan Roll', 'Paneer Schezwan Roll', 'Vada Pav',
                            'Veg Frankie', 'Veg Schezwan Frankie', 'Paneer Frankie', 'Schezwan Corn Frankie',
                            'Paneer Schezwan Frankie', 'Babycorn Schezwan Frankie', 'Veg Cheese Frankie', 'Mushroom Frankie',
                            'Masala Maggie', 'Corn Masala Maggie', 'Paneer Masala Maggie', 'Babycorn Masala Maggie',
                            'Potato Masala Maggie', 'Cheese Masala Maggie', 'Bread Burji']
            if item_name in veg_keywords:
                category = 'veg'
            
            # Determine section (use subsection if available, otherwise main section)
            section = current_subsection if current_subsection else current_section
            
            # Generate description
            description = f"{item_name}"
            
            # Determine image
            image = 'default.jpg'
            if 'dosa' in item_name.lower():
                image = 'dosa.jpg'
            elif 'idli' in item_name.lower() or 'idly' in item_name.lower():
                image = 'idli.jpg'
            elif 'vada' in item_name.lower():
                image = 'vada.jpg'
            elif 'bath' in item_name.lower():
                image = 'bath.jpg'
            elif 'poori' in item_name.lower():
                image = 'poori.jpg'
            elif 'noodles' in item_name.lower():
                image = 'noodles.jpg'
            elif 'rice' in item_name.lower() and 'fried' in item_name.lower():
                image = 'friedrice.jpg'
            elif 'manchurian' in item_name.lower():
                image = 'manchurian.jpg'
            elif 'juice' in item_name.lower():
                image = 'juice.jpg'
            elif 'shake' in item_name.lower():
                image = 'milkshake.jpg'
            elif 'ice cream' in item_name.lower():
                image = 'icecream.jpg'
            elif 'sandwich' in item_name.lower():
                image = 'sandwich.jpg'
            elif 'burger' in item_name.lower():
                image = 'burger.jpg'
            elif 'roll' in item_name.lower():
                image = 'roll.jpg'
            elif 'frankie' in item_name.lower():
                image = 'frankie.jpg'
            elif 'maggie' in item_name.lower():
                image = 'maggie.jpg'
            elif 'omlet' in item_name.lower() or 'omelette' in item_name.lower():
                image = 'omelette.jpg'
            elif 'puri' in item_name.lower():
                image = 'puri.jpg'
            elif 'samosa' in item_name.lower():
                image = 'samosa.jpg'
            elif 'coffee' in item_name.lower() or 'tea' in item_name.lower():
                image = 'tea.jpg'
            
            menu_items.append((1, item_name, description, price, category, image, section))

# Generate Python code for db_setup.py
print(f"# Total items parsed: {len(menu_items)}\n")
print("    vidhyarthi_khaana_items = [")
for item in menu_items:
    canteen_id, name, desc, price, cat, img, section = item
    # Escape single quotes in name, description, and section
    name = name.replace("'", "\\'")
    desc = desc.replace("'", "\\'")
    section = section.replace("'", "\\'")
    print(f"        (1, '{name}', '{desc}', {price}, '{cat}', '{img}', '{section}'),")
print("    ]")

print(f"\n# Total items: {len(menu_items)}")
