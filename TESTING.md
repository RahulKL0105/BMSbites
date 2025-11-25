# BMS Bites - Testing Guide

## 🚀 Quick Start

### 1. Start the Server

**Open Terminal** and run:
```bash
cd /Users/rahulkl/Projects/bmsbites
python3 app.py
```

You should see:
```
============================================================
🍔 BMS Bites - College Canteen Ordering System
============================================================

📊 Features:
  ✓ Pandas/NumPy for menu operations & analytics
  ✓ SQLite3 database with 30+ menu items
  ✓ User authentication (Customer & Admin roles)
  ✓ Real-time order tracking
  ✓ Admin dashboard with sales analytics
  ✓ Recommendation engine

🔑 Default Credentials:
  Admin  - username: admin, password: admin123
  User   - username: rahul, password: user123

🌐 Starting server on http://127.0.0.1:5001
============================================================

 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5001
 * Running on http://192.168.x.x:5001
```

### 2. Open in Browser

Visit: **http://localhost:5001**

---

## 🧪 Testing Checklist

### ✅ Homepage Testing

**What to Check**:
- [ ] Page loads successfully
- [ ] See "Welcome to BMS Bites 🍔" heading
- [ ] Carousel with food images is visible
- [ ] **3 canteen cards** are displayed:
  - Main Canteen
  - Food Court
  - Juice Center
- [ ] Each card shows location and "Order Now" button
- [ ] Navigation bar shows "BMS Bites" logo
- [ ] Login/Sign Up links visible in navbar

**Screenshot Location**: 
![Homepage](file:///Users/rahulkl/.gemini/antigravity/brain/813eca42-187b-46f7-a599-a3763c4923ed/canteen_selection_page_1764005156670.png)

---

### ✅ Canteen Selection Testing

**Steps**:
1. Click "Order Now" on **Main Canteen** card
2. You should be redirected to `/menu`
3. Flash message: "Selected Main Canteen"

**What to Check**:
- [ ] Menu page loads
- [ ] Header shows: "Main Canteen - Menu"
- [ ] Location shown: "Near Library Block"
- [ ] "Change Canteen" button visible
- [ ] Menu items displayed (should see ~11 items)

**Screenshot Location**:
![Menu Page](file:///Users/rahulkl/.gemini/antigravity/brain/813eca42-187b-46f7-a599-a3763c4923ed/main_canteen_menu_1764005193278.png)

---

### ✅ Menu Browsing Testing

**Filters to Test**:

1. **Category Filter**:
   - [ ] Select "Veg" - only vegetarian items show
   - [ ] Select "Non-Veg" - only non-veg items show
   - [ ] Select "Beverages" - only drinks show
   - [ ] Select "All Categories" - all items show

2. **Sort Filter**:
   - [ ] "Name (A-Z)" - items sorted alphabetically
   - [ ] "Price (Low-High)" - cheapest items first
   - [ ] "Price (High-Low)" - expensive items first

3. **Menu Items Display**:
   - [ ] Each card shows:
     - Food image (or placeholder)
     - Item name
     - Description
     - Price in ₹
     - Category badge (green=veg, red=non-veg, blue=beverage)
     - "Add to Cart" button

---

### ✅ Shopping Cart Testing

**Steps**:
1. Click "Add to Cart" on any item (e.g., "Masala Dosa")
2. Flash message: "Item added to cart"
3. Cart badge in navbar shows count (e.g., "1")
4. Click cart icon in navbar

**What to Check**:
- [ ] Cart page loads
- [ ] Item appears with:
  - Image
  - Name and price
  - Quantity controls (+/-)
  - Remove button
  - Item total
- [ ] Order Summary shows total price
- [ ] "Proceed to Checkout" button visible

**Test Quantity Controls**:
- [ ] Click "+" - quantity increases, total updates
- [ ] Click "-" - quantity decreases
- [ ] Click "-" when qty=1 - item removed
- [ ] Click trash icon - item removed immediately

**Test Recommendations** (if no orders exist yet):
- [ ] "You might also like" section shows 3 random items
- [ ] Can add recommended items to cart

---

### ✅ Authentication Testing

#### Sign Up Test

**Steps**:
1. Click "Sign Up" in navbar
2. Enter:
   - Username: `testuser`
   - Password: `test123`
3. Click "Create Account"

**Expected**:
- [ ] Flash message: "Registration successful! Please login."
- [ ] Redirected to login page

#### Login Test (Customer)

**Steps**:
1. Click "Login"
2. Enter:
   - Username: `rahul`
   - Password: `user123`
3. Click "Login"

**Expected**:
- [ ] Flash message: "Logged in successfully!"
- [ ] Navbar shows username "rahul" with dropdown
- [ ] Dropdown has "My Orders" and "Logout"

#### Login Test (Admin)

**Steps**:
1. Logout first
2. Login with:
   - Username: `admin`
   - Password: `admin123`

**Expected**:
- [ ] Navbar shows "Dashboard" link
- [ ] Username dropdown shows "admin"

---

### ✅ Checkout & Order Testing

**Prerequisites**: Must be logged in

**Steps**:
1. Add items to cart (at least 2-3 items)
2. Go to cart
3. Click "Proceed to Checkout"

**Checkout Page**:
- [ ] Shows payment form (simulated)
- [ ] Card number field
- [ ] Expiry date field
- [ ] CVV field
- [ ] Info alert: "This is a simulated payment gateway"

**Place Order**:
1. Enter any fake card details:
   - Card: `1234 5678 9012 3456`
   - Expiry: `12/25`
   - CVV: `123`
2. Click "Pay & Place Order"

**Expected**:
- [ ] Flash message: "Order #X placed successfully!"
- [ ] Redirected to "My Orders" page
- [ ] Cart is now empty (badge shows 0)

---

### ✅ Order Tracking Testing

**Steps**:
1. Click username dropdown → "My Orders"

**What to Check**:
- [ ] Order appears in list
- [ ] Shows:
  - Order ID
  - Total amount
  - Status badge (yellow="KITCHEN")
  - Timestamp
- [ ] Click on order to view details

**Order Detail Page**:
- [ ] Shows order number
- [ ] Status badge
- [ ] Table with:
  - Item names
  - Quantities
  - Prices
  - Total amount
- [ ] "Back to Orders" button

---

### ✅ Admin Dashboard Testing

**Prerequisites**: Login as admin

**Steps**:
1. Click "Dashboard" in navbar

**What to Check**:

**Summary Cards**:
- [ ] Total Revenue (if orders exist)
- [ ] Total Orders count
- [ ] Average Order Value

**Top Selling Items**:
- [ ] Shows items with quantity sold
- [ ] Only appears if orders exist

**Management Buttons**:
- [ ] "Manage Menu" button
- [ ] "Manage Orders" button

**Recent Orders Table**:
- [ ] Shows last 10 orders
- [ ] Columns: ID, User, Amount, Status, Time, Action
- [ ] "View" button for each order

---

### ✅ Menu Management Testing (Admin)

**Steps**:
1. Dashboard → "Manage Menu"

**View Menu**:
- [ ] Table shows all menu items
- [ ] Columns: Image, Name, Canteen, Category, Price, Status, Actions
- [ ] Edit and Delete buttons for each item

**Add New Item**:
1. Click "+ Add New Item"
2. Fill form:
   - Canteen: Main Canteen
   - Name: `Test Pizza`
   - Description: `Delicious test pizza`
   - Price: `150`
   - Category: `veg`
   - Image URL: `pizza.jpg`
3. Click "Add Item"

**Expected**:
- [ ] Flash: "Item added"
- [ ] New item appears in table
- [ ] Item shows in menu when you browse

**Edit Item**:
1. Click edit icon (pencil) on any item
2. Change price to `200`
3. Click "Save Changes"

**Expected**:
- [ ] Flash: "Item updated"
- [ ] Price updated in table

**Delete Item**:
1. Click delete icon (trash)
2. Confirm deletion

**Expected**:
- [ ] Flash: "Item deleted"
- [ ] Item removed from table

---

### ✅ Order Management Testing (Admin)

**Steps**:
1. Dashboard → "Manage Orders"

**What to Check**:
- [ ] Table shows all orders
- [ ] Columns: ID, User, Amount, Status, Time, Update Status, Details
- [ ] Status dropdown for each order
- [ ] "View" button

**Update Order Status**:
1. Find an order with status "KITCHEN"
2. Change dropdown to "Prepared"
3. Click "Update"

**Expected**:
- [ ] Flash: "Order status updated"
- [ ] Badge color changes (yellow → blue)

**Test All Statuses**:
- [ ] Kitchen (yellow badge)
- [ ] Prepared (blue badge)
- [ ] Completed (green badge)

---

### ✅ Multi-Canteen Testing

**Test Different Canteens**:

1. **Main Canteen**:
   - [ ] Select Main Canteen
   - [ ] Should see ~11 items (Dosa, Biryani, etc.)

2. **Food Court**:
   - [ ] Click "Change Canteen" or go to homepage
   - [ ] Select Food Court
   - [ ] Should see ~12 items (Burgers, Fries, etc.)

3. **Juice Center**:
   - [ ] Select Juice Center
   - [ ] Should see ~10 items (Beverages, Juices, etc.)

**Verify**:
- [ ] Each canteen shows different menu
- [ ] Selected canteen persists when navigating
- [ ] Can add items from one canteen at a time
- [ ] Order shows which canteen it's from

---

### ✅ Session Persistence Testing

**Test Cart Persistence**:
1. Add items to cart
2. Navigate to different pages
3. Return to cart

**Expected**:
- [ ] Cart items still there
- [ ] Quantities preserved

**Test Canteen Selection**:
1. Select a canteen
2. Browse menu
3. Go to homepage and back to menu

**Expected**:
- [ ] Same canteen still selected
- [ ] No need to reselect

---

### ✅ Responsive Design Testing

**Test on Different Screen Sizes**:

1. **Desktop** (1920x1080):
   - [ ] 3 canteen cards per row
   - [ ] 3 menu items per row
   - [ ] Navbar fully expanded

2. **Tablet** (768px):
   - [ ] 2 canteen cards per row
   - [ ] 2 menu items per row
   - [ ] Navbar hamburger menu

3. **Mobile** (375px):
   - [ ] 1 canteen card per row
   - [ ] 1 menu item per row
   - [ ] Stacked layout

---

## 🎥 Video Recording

A recording of the website in action has been saved:
![Demo Recording](file:///Users/rahulkl/.gemini/antigravity/brain/813eca42-187b-46f7-a599-a3763c4923ed/bmsbites_demo_1764005127481.webp)

---

## 🐛 Troubleshooting

### Server Won't Start

**Error**: `Address already in use`
```bash
# Find and kill process on port 5001
lsof -ti:5001 | xargs kill -9

# Or change port in app.py line 32
```

### Database Errors

**Error**: `no such table: canteens`
```bash
# Reinitialize database
python3 database/db_setup.py
```

### Images Not Loading

- Images show placeholder (this is normal)
- To add real images, place them in `static/img/`

### Login Not Working

**Error**: `Invalid username or password`
- Check credentials:
  - Admin: `admin` / `admin123`
  - User: `rahul` / `user123`
- Username is case-sensitive

### Menu Not Showing

- Make sure you selected a canteen first
- Check if items have `is_available = 1`

---

## 📊 Test Results Template

```
✅ Homepage: PASS
✅ Canteen Selection: PASS
✅ Menu Browsing: PASS
✅ Cart Functionality: PASS
✅ Authentication: PASS
✅ Checkout: PASS
✅ Order Tracking: PASS
✅ Admin Dashboard: PASS
✅ Menu Management: PASS
✅ Order Management: PASS
✅ Multi-Canteen: PASS
```

---

## 🎯 Key Features to Demonstrate

1. **Pandas Usage**: 
   - Filter menu by category (see network tab)
   - Sort by price
   - View analytics dashboard

2. **NumPy Usage**:
   - Admin dashboard revenue calculations
   - Average order value

3. **Multi-Canteen**:
   - Select different canteens
   - See different menus
   - Orders track canteen

4. **Real-time Updates**:
   - Cart badge updates
   - Order status changes
   - Flash messages

---

## 📝 Notes

- **Server must be running** for website to work
- **Database resets** when you run `db_setup.py`
- **Session data** clears when you close browser
- **Port 5001** must be available

---

**Happy Testing!** 🎉

For issues, check `README.md` or `TECHNICAL.md`
