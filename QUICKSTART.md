# BMS Bites - Quick Start Guide

## 🚀 Running the Application

The application is currently **RUNNING** on: **http://127.0.0.1:5001**

### Start Server
```bash
cd /Users/rahulkl/Projects/bmsbites
python3 app.py
```

### Stop Server
Press `Ctrl+C` in the terminal

## 🔑 Login Credentials

### Admin Account
- **URL**: http://127.0.0.1:5001/login
- **Username**: `admin`
- **Password**: `admin123`
- **Access**: Dashboard, Analytics, Menu Management, Order Management

### Customer Account
- **URL**: http://127.0.0.1:5001/login
- **Username**: `rahul`
- **Password**: `user123`
- **Access**: Browse Menu, Order Food, Track Orders

## 📋 Quick Test Flow

### Customer Journey
1. Visit http://127.0.0.1:5001
2. Click "Menu" or "Order Now"
3. Filter by category (Veg/Non-Veg/Beverage)
4. Add items to cart
5. View cart - see recommendations
6. Checkout (use any fake card details)
7. View "My Orders" to track status

### Admin Journey
1. Login as admin
2. View Dashboard - see analytics (revenue, top items)
3. Click "Manage Menu" - add/edit/delete items
4. Click "Manage Orders" - update order status
5. See real-time updates

## 📊 Pandas/NumPy Features

### Menu Operations
- **File**: `utils/menu_manager.py`
- Filter menu by category using Pandas
- Sort by price/name using DataFrame operations
- Convert SQL to Pandas DataFrame

### Analytics
- **File**: `utils/analytics.py`
- Revenue calculations with NumPy (sum, mean)
- Top selling items with Pandas groupby
- Daily revenue with datetime operations
- Recommendations using NumPy filtering

## 🗂️ Project Structure

```
bmsbites/
├── app.py                 # Main application (port 5001)
├── config.py              # Settings
├── requirements.txt       # Dependencies
├── database/
│   ├── schema.sql        # DB schema
│   ├── db_setup.py       # Initialization
│   └── bmsbites.db       # SQLite database (30+ items)
├── routes/               # 4 blueprints
├── utils/                # 3 Pandas/NumPy modules
├── templates/            # 11 HTML pages
└── static/               # CSS + JS
```

## 🔧 Troubleshooting

### Port Already in Use
If port 5001 is busy, edit `app.py` line 32:
```python
app.run(debug=True, host='0.0.0.0', port=5002)  # Change port
```

### Reset Database
```bash
python3 database/db_setup.py
```

### Missing Dependencies
```bash
pip3 install -r requirements.txt
```

## ✨ Key Features

✅ User authentication with sessions
✅ Role-based access (Customer/Admin)
✅ Menu filtering & sorting with Pandas
✅ Shopping cart with recommendations
✅ Order tracking (Kitchen → Prepared → Completed)
✅ Admin dashboard with NumPy analytics
✅ Real-time AJAX updates
✅ Responsive Bootstrap UI
✅ 30+ seeded menu items

## 📖 Full Documentation

See `README.md` for complete documentation
See `walkthrough.md` for detailed feature explanation

---

**Server Status**: ✅ Running on http://127.0.0.1:5001
