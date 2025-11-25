# Fix category issues in parsed menu
import re

# Read the parsed file
with open('vidhyarthi_items_only.txt', 'r') as f:
    content = f.read()

# Fix categories for items that should be 'veg' but are marked as 'non-veg'
veg_keywords = ['Veg Roll', 'Paneer Roll', 'Paneer Cheese Roll', 'Mushroom Roll', 'Mushroom Cheese Roll', 
                'Babycorn Roll', 'Schezwan Roll', 'Paneer Schezwan Roll', 'Vada Pav',
                'Veg Frankie', 'Veg Schezwan Frankie', 'Paneer Frankie', 'Schezwan Corn Frankie',
                'Paneer Schezwan Frankie', 'Babycorn Schezwan Frankie', 'Veg Cheese Frankie', 'Mushroom Frankie',
                'Masala Maggie', 'Corn Masala Maggie', 'Paneer Masala Maggie', 'Babycorn Masala Maggie',
                'Potato Masala Maggie', 'Cheese Masala Maggie', 'Bread Burji']

for keyword in veg_keywords:
    # Replace 'non-veg' with 'veg' for these specific items
    pattern = f"(\\(1, '{re.escape(keyword)}', '{re.escape(keyword)}', \\d+\\.0, )'non-veg'(,)"
    content = re.sub(pattern, r"\1'veg'\2", content)

# Write the fixed content
with open('vidhyarthi_items_fixed.txt', 'w') as f:
    f.write(content)

print("Fixed categories for vegetarian items")
print("Output written to vidhyarthi_items_fixed.txt")
