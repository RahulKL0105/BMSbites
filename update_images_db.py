#!/usr/bin/env python3
# Update db_setup.py to use the generated and downloaded images

import re

# Read db_setup.py
with open('database/db_setup.py', 'r') as f:
    content = f.read()

# Define mappings
# Format: (Section Name, Image Filename)
section_mappings = {
    'SOUTH INDIAN BREAKFAST': 'south_indian_breakfast.png',
    'Dosa Items': 'masala_dosa.png',
    'MEALS - PAROTA / RICE': 'meals_thali.png',
    'FRESH JUICE': 'juice.jpg',
    'MILK SHAKES': 'milkshake.jpg',
    'ICE CREAM / MILK SHAKE': 'icecream.jpg',
    'CHATS': 'chat.jpg',
}

# Specific keyword mappings for Chinese section
chinese_mappings = {
    'Rice': 'veg_fried_rice.png',
    'Manchurian': 'manchurian.jpg',
    'default': 'veg_noodles.png'
}

# Specific keyword mappings for mixed sections
mixed_mappings = {
    'Omlet': 'omelette.jpg',
    'Egg': 'omelette.jpg',
    'Roll': 'frankie.jpg',
    'Frankie': 'frankie.jpg',
    'Sandwich': 'sandwich.jpg',
    'Maggie': 'maggie.jpg',
    'Poori': 'poori.jpg',
    'Coffee': 'coffee.jpg',
    'Tea': 'coffee.jpg',
    'Buns': 'poori.jpg',
    'Bajji': 'poori.jpg',
}

def replace_image(match):
    # match.group(1) = start of line until image_url
    # match.group(2) = image_url
    # match.group(3) = rest of line including section
    
    full_match = match.group(0)
    
    # Extract section
    section_match = re.search(r"', '([^']+)'\),", full_match)
    if not section_match:
        return full_match
    
    section = section_match.group(1)
    
    # Extract name
    name_match = re.search(r"\d+, '([^']+)',", full_match)
    name = name_match.group(1) if name_match else ""
    
    new_image = None
    
    # Check for specific item keywords first (highest priority)
    for keyword, image in mixed_mappings.items():
        if keyword in name:
            new_image = image
            break
            
    # If no specific keyword match, check section mappings
    if not new_image:
        if section in section_mappings:
            new_image = section_mappings[section]
        elif 'CHINESE' in section:
            if 'Rice' in name:
                new_image = chinese_mappings['Rice']
            elif 'Manchurian' in name:
                new_image = chinese_mappings['Manchurian']
            else:
                new_image = chinese_mappings['default']
            
    if new_image:
        # Replace the image in the string
        # Look for the image part: 'something.jpg' or 'something.png'
        return re.sub(r"'[^']+\.(jpg|png)'", f"'{new_image}'", full_match)
    
    return full_match

# Regex to find menu item lines
# (1, 'Name', 'Desc', 10.0, 'cat', 'img.jpg', 'Section'),
pattern = r"\s+\(\d+, '[^']+', '[^']+', \d+\.\d+, '[^']+', '[^']+', '[^']+'\),"

content = re.sub(pattern, replace_image, content)

# Write back
with open('database/db_setup.py', 'w') as f:
    f.write(content)

print("Successfully updated db_setup.py with variety images")
