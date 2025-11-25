# User Modification Guide - BMS Bites

This guide explains how to customize and modify the BMS Bites application for your needs.

## 📝 Table of Contents
1. [Changing Menu Items](#changing-menu-items)
2. [Adding Food Images](#adding-food-images)
3. [Managing Canteens](#managing-canteens)
4. [Customizing Prices](#customizing-prices)
5. [Adding New Categories](#adding-new-categories)
6. [User Management](#user-management)

---

## 🍽️ Changing Menu Items

### Method 1: Using Admin Dashboard (Recommended)

1. **Login as Admin**
   - Go to http://localhost:5001/login
   - Username: `admin`
   - Password: `admin123`

2. **Navigate to Menu Management**
   - Click "Dashboard" in navigation
   - Click "Manage Menu" button

3. **Add New Item**
   - Click "+ Add New Item" button
   - Fill in the form:
     - **Canteen**: Select which canteen (Main Canteen, Food Court, or Juice Center)
     - **Name**: Item name (e.g., "Paneer Tikka")
     - **Description**: Brief description
     - **Price**: Amount in rupees
     - **Category**: veg, non-veg, or beverage
     - **Image URL**: Filename (e.g., "paneer_tikka.jpg")
   - Click "Add Item"

4. **Edit Existing Item**
   - Find the item in the table
   - Click the edit icon (pencil)
   - Modify any field
   - Click "Save Changes"

5. **Delete Item**
   - Click the delete icon (trash)
   - Confirm deletion

### Method 2: Direct Database Modification

**File**: `database/db_setup.py`

**Location**: Lines 30-90 (menu items lists)

**Example - Adding to Main Canteen**:
```python
main_canteen_items = [
    # Existing items...
    (1, 'Paneer Tikka', 'Grilled cottage cheese', 140.0, 'veg', 'paneer_tikka.jpg'),
    # Add your new item here ↑
]
```

**Parameters**:
- `1` = Canteen ID (1=Main, 2=Food Court, 3=Juice Center)
- `'Paneer Tikka'` = Item name
- `'Grilled cottage cheese'` = Description
- `140.0` = Price
- `'veg'` = Category (veg/non-veg/beverage)
- `'paneer_tikka.jpg'` = Image filename

**After modifying**, reinitialize database:
```bash
python3 database/db_setup.py
```

⚠️ **Warning**: This will reset ALL data including orders!

---

## 🖼️ Adding Food Images

### Step 1: Prepare Images

1. **Image Requirements**:
   - Format: JPG, PNG, or WebP
   - Recommended size: 300x200 pixels
   - Keep file size under 200KB for faster loading

2. **Naming Convention**:
   - Use lowercase
   - No spaces (use underscores)
   - Example: `chicken_biryani.jpg`, `cold_coffee.png`

### Step 2: Add to Project

1. **Copy image to static folder**:
   ```bash
   cp your_image.jpg /Users/rahulkl/Projects/bmsbites/static/img/
   ```

2. **Or manually**:
   - Navigate to `/Users/rahulkl/Projects/bmsbites/static/img/`
   - Paste your image file there

### Step 3: Link to Menu Item

**Option A: Via Admin Dashboard**
- Edit the menu item
- In "Image URL" field, enter just the filename: `your_image.jpg`

**Option B: In Database Setup**
- Update the image_url parameter in `db_setup.py`
- Example: `('Burger', 'Veg burger', 70.0, 'veg', 'my_burger.jpg')`

### Fallback Behavior

If image is missing, a placeholder will show automatically. No errors!

---

## 🏪 Managing Canteens

### Adding a New Canteen

**File**: `database/db_setup.py`

**Location**: Lines 25-30

```python
canteens = [
    ('Main Canteen', 'Near Library Block', 'Largest canteen', '8:00 AM', '8:00 PM', 1),
    ('Food Court', 'Behind Auditorium', 'Fast food', '9:00 AM', '6:00 PM', 1),
    ('Juice Center', 'Sports Complex', 'Beverages', '7:00 AM', '7:00 PM', 1),
    # Add new canteen here:
    ('Night Canteen', 'Hostel Block', 'Late night food', '8:00 PM', '2:00 AM', 1),
]
```

**Parameters**:
1. Name
2. Location
3. Description
4. Opening time
5. Closing time
6. Is open (1=yes, 0=no)

### Modifying Canteen Details

**Via Database**:
```sql
UPDATE canteens 
SET opening_time='7:00 AM', closing_time='9:00 PM' 
WHERE id=1;
```

**Via Python**:
```python
import sqlite3
conn = sqlite3.connect('database/bmsbites.db')
cursor = conn.cursor()
cursor.execute("UPDATE canteens SET name='New Name' WHERE id=1")
conn.commit()
```

---

## 💰 Customizing Prices

### Bulk Price Update

**Increase all prices by 10%**:
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect('database/bmsbites.db')
df = pd.read_sql_query("SELECT * FROM menu", conn)
df['price'] = df['price'] * 1.10  # 10% increase
df.to_sql('menu', conn, if_exists='replace', index=False)
conn.close()
```

### Category-wise Pricing

**Discount on beverages**:
```python
cursor.execute("UPDATE menu SET price = price * 0.9 WHERE category='beverage'")
```

### Individual Item

Via admin dashboard or:
```python
cursor.execute("UPDATE menu SET price=150 WHERE name='Chicken Biryani'")
```

---

## 🏷️ Adding New Categories

### Step 1: Add to Database

**File**: `database/db_setup.py`

Add items with new category:
```python
(1, 'Ice Cream', 'Vanilla ice cream', 50.0, 'dessert', 'icecream.jpg'),
```

### Step 2: Update Filter UI

**File**: `templates/menu.html`

**Location**: Lines 10-15

```html
<select name="category" class="form-select">
    <option value="all">All Categories</option>
    <option value="veg">Veg</option>
    <option value="non-veg">Non-Veg</option>
    <option value="beverage">Beverages</option>
    <!-- Add new category -->
    <option value="dessert">Desserts</option>
</select>
```

### Step 3: Update Admin Forms

**File**: `templates/manage_menu.html`

Add to both Add and Edit modals (around lines 136 and 80):
```html
<option value="dessert">Dessert</option>
```

---

## 👥 User Management

### Adding New Admin

**Method 1: Via Python Script**
```python
from werkzeug.security import generate_password_hash
import sqlite3

conn = sqlite3.connect('database/bmsbites.db')
cursor = conn.cursor()

password_hash = generate_password_hash('newadmin123')
cursor.execute(
    "INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
    ('newadmin', password_hash, 'admin')
)
conn.commit()
```

**Method 2: Via Database Setup**

**File**: `database/db_setup.py`

**Location**: Lines 15-23

```python
# Add after existing admin
new_admin_pass = generate_password_hash('password123')
cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
               ('manager', new_admin_pass, 'admin'))
```

### Adding New Customer

Customers can self-register via signup page, or add manually:
```python
user_pass = generate_password_hash('user123')
cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
               ('john', user_pass, 'customer'))
```

### Changing Password

```python
new_password_hash = generate_password_hash('newpassword123')
cursor.execute("UPDATE users SET password_hash=? WHERE username=?",
               (new_password_hash, 'admin'))
```

---

## 🎨 Customizing Appearance

### Changing Colors

**File**: `static/css/style.css`

**Location**: Lines 1-7

```css
:root {
    --primary-color: #2c3e50;    /* Change navbar color */
    --secondary-color: #e74c3c;  /* Change accent color */
    --success-color: #27ae60;    /* Change success messages */
}
```

### Changing Logo/Branding

**File**: `templates/layout.html`

**Location**: Line 15

```html
<a class="navbar-brand" href="{{ url_for('main.index') }}">
    <i class="fas fa-utensils me-2"></i>Your College Name
</a>
```

---

## 🔧 Advanced Modifications

### Changing Port Number

**File**: `app.py`

**Location**: Line 32

```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Change 5001 to your port
```

### Adding New Fields to Menu

1. **Update Schema** (`database/schema.sql`):
```sql
ALTER TABLE menu ADD COLUMN spice_level TEXT;
```

2. **Update Forms** (`templates/manage_menu.html`)
3. **Update Display** (`templates/menu.html`)

---

## 📋 Quick Reference

### File Locations

| What to Change | File Path |
|----------------|-----------|
| Menu Items | `database/db_setup.py` |
| Images | `static/img/` |
| Canteens | `database/db_setup.py` |
| Prices | Admin Dashboard or `db_setup.py` |
| Colors/Styles | `static/css/style.css` |
| Page Layout | `templates/*.html` |
| Business Logic | `utils/*.py` |
| Routes/URLs | `routes/*.py` |

### Common Commands

```bash
# Reinitialize database
python3 database/db_setup.py

# Start server
python3 app.py

# Install dependencies
pip3 install -r requirements.txt
```

---

## ⚠️ Important Notes

1. **Backup Before Changes**: Always backup `database/bmsbites.db` before modifications
2. **Test Locally**: Test all changes on local machine before deploying
3. **Image Optimization**: Compress images to improve load times
4. **Price Consistency**: Ensure prices are realistic and consistent
5. **Database Reset**: Running `db_setup.py` will DELETE all existing data

---

## 🆘 Troubleshooting

### Images Not Showing
- Check filename matches exactly (case-sensitive)
- Verify image is in `static/img/` folder
- Clear browser cache

### Menu Items Not Appearing
- Check `is_available` is set to 1
- Verify canteen_id matches selected canteen
- Refresh page

### Price Changes Not Saving
- Ensure using float values (e.g., 50.0 not 50)
- Check database connection
- Verify admin permissions

---

**Need Help?** Check `TECHNICAL.md` for implementation details or `README.md` for general information.
