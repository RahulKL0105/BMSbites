#!/usr/bin/env python3
# Update db_setup.py with the complete 225-item menu

# Read the fixed items
with open('vidhyarthi_items_fixed.txt', 'r') as f:
    new_items = f.read()

# Read the current db_setup.py
with open('database/db_setup.py', 'r') as f:
    lines = f.readlines()

# Find the start and end of vidhyarthi_khaana_items
start_idx = None
end_idx = None

for i, line in enumerate(lines):
    if 'vidhyarthi_khaana_items = [' in line:
        start_idx = i
    if start_idx is not None and '# Seed Menu Items for Gowdas Canteen' in line:
        end_idx = i
        break

if start_idx is None or end_idx is None:
    print("Error: Could not find the vidhyarthi_khaana_items section")
    exit(1)

# Replace the section
new_lines = lines[:start_idx] + [f"    # Seed Menu Items for Vidhyarthi Khaana (ID: 1) - Complete Menu with 225 items\n"] + [f"    {new_items}\n\n"] + lines[end_idx:]

# Write back
with open('database/db_setup.py', 'w') as f:
    f.writelines(new_lines)

# Update the total count message
with open('database/db_setup.py', 'r') as f:
    content = f.read()

# Update the success message to reflect 225 + 15 = 240 items
content = content.replace('✓ 49 Menu items distributed across canteens', '✓ 240 Menu items distributed across canteens')

with open('database/db_setup.py', 'w') as f:
    f.write(content)

print("Successfully updated db_setup.py with 225 Vidhyarthi Khaana items")
print("Total menu items: 240 (225 Vidhyarthi Khaana + 15 Gowdas Canteen)")
