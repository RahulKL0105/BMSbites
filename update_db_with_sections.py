#!/usr/bin/env python3
# Update db_setup.py with menu items including category sections

# Read the parsed items with sections
with open('parsed_menu_with_sections.txt', 'r') as f:
    content = f.read()

# Extract just the items list
start = content.find('vidhyarthi_khaana_items = [')
end = content.find(']', start) + 1
new_items_section = content[start:end]

# Read the current db_setup.py
with open('database/db_setup.py', 'r') as f:
    db_setup_content = f.read()

# Find and replace the vidhyarthi_khaana_items section
import re

# Pattern to match the entire vidhyarthi_khaana_items assignment
pattern = r'vidhyarthi_khaana_items = \[.*?\n    \]'

# Replace with new items (need to adjust indentation)
new_items_indented = new_items_section.replace('\n    ', '\n    ')  # Ensure proper indentation

db_setup_content = re.sub(pattern, new_items_indented, db_setup_content, flags=re.DOTALL)

# Update the executemany statement to include category_section
old_insert = 'cursor.executemany("INSERT INTO menu (canteen_id, name, description, price, category, image_url) VALUES (?, ?, ?, ?, ?, ?)", all_items)'
new_insert = 'cursor.executemany("INSERT INTO menu (canteen_id, name, description, price, category, image_url, category_section) VALUES (?, ?, ?, ?, ?, ?, ?)", all_items)'

db_setup_content = db_setup_content.replace(old_insert, new_insert)

# Write back
with open('database/db_setup.py', 'w') as f:
    f.write(db_setup_content)

print("Successfully updated db_setup.py with category sections")
print("Total items: 225 Vidhyarthi Khaana items with section headers")
