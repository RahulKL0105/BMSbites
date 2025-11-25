import re

# Read the menu file
with open('VIDHYARTHI_KHANA_menu.txt', 'r') as f:
    lines = f.readlines()

menu_items = []
current_section = ''

for line in lines:
    line = line.strip()
    
    # Skip empty lines and headers
    if not line or line.startswith('VIDHYARTHI') or line.startswith('BMS College') or line.startswith('South Indian /'):
        continue
    
    # Track section headers
    if line.isupper() or line.startswith('(Board'):
        current_section = line
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
            
            menu_items.append((1, item_name, description, price, category, image))

# Generate Python code for db_setup.py
print(f"# Total items parsed: {len(menu_items)}\n")
print("vidhyarthi_khaana_items = [")
for item in menu_items:
    canteen_id, name, desc, price, cat, img = item
    # Escape single quotes in name and description
    name = name.replace("'", "\\'")
    desc = desc.replace("'", "\\'")
    print(f"    ({canteen_id}, '{name}', '{desc}', {price}, '{cat}', '{img}'),")
print("]")

print(f"\n# Total items: {len(menu_items)}")
