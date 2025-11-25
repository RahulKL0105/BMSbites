# BMS Bites - College Canteen Food Ordering Platform

A complete production-ready fullstack web application for college canteen food ordering built with Flask, SQLite, Pandas, and NumPy.

## 🚀 Features

### Core Functionality
- **User Roles**: Customer and Admin with role-based access control
- **Authentication**: Secure login/signup with password hashing
- **Menu Management**: Browse, filter, and sort menu items
- **Shopping Cart**: Add items, update quantities, view recommendations
- **Order System**: Place orders, track status, view history
- **Real-time Updates**: Live order status updates via AJAX
- **Admin Dashboard**: Comprehensive analytics and management tools

### Technology Stack
- **Backend**: Python 3 + Flask
- **Database**: SQLite3
- **Data Processing**: Pandas + NumPy (for menu operations, analytics, recommendations)
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Session Management**: Flask sessions with secure cookies

## 📊 Pandas & NumPy Usage

This application extensively uses Pandas and NumPy throughout:

### Menu Operations (`utils/menu_manager.py`)
- Read menu from SQLite into Pandas DataFrame
- Filter menu by category, price range using Pandas
- Sort menu items using DataFrame operations
- Convert data to JSON for API responses

### Analytics (`utils/analytics.py`)
- **Sales Summary**: Calculate total revenue, order count, average order value using NumPy
- **Top Selling Items**: Group and aggregate order data with Pandas
- **Daily Revenue**: Time-series analysis with Pandas datetime operations
- **Recommendations**: Simple collaborative filtering using NumPy calculations

### Order Processing (`utils/order_manager.py`)
- Order data manipulation with Pandas
- Price calculations and summaries

## 📁 Project Structure

```
bmsbites/
├── app.py                  # Main Flask application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── database/
│   ├── schema.sql         # Database schema
│   ├── db_setup.py        # Database initialization & seed data
│   └── bmsbites.db        # SQLite database (created on setup)
├── routes/
│   ├── auth.py            # Authentication routes
│   ├── main.py            # Customer routes
│   ├── admin.py           # Admin routes
│   └── api.py             # API endpoints
├── utils/
│   ├── menu_manager.py    # Menu operations with Pandas
│   ├── analytics.py       # Analytics with Pandas/NumPy
│   └── order_manager.py   # Order processing
├── templates/
│   ├── layout.html        # Base template
│   ├── index.html         # Landing page
│   ├── login.html         # Login page
│   ├── signup.html        # Signup page
│   ├── menu.html          # Menu browsing
│   ├── cart.html          # Shopping cart
│   ├── checkout.html      # Checkout page
│   ├── orders.html        # Order history
│   ├── order_detail.html  # Order details
│   ├── dashboard.html     # Admin dashboard
│   ├── manage_menu.html   # Menu management
│   └── manage_orders.html # Order management
└── static/
    ├── css/
    │   └── style.css      # Custom styles
    ├── js/
    │   └── main.js        # JavaScript for interactivity
    └── img/               # Food images (placeholder)
```

## 🛠️ Setup Instructions

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or navigate to the project directory**
   ```bash
   cd /Users/rahulkl/Projects/bmsbites
   ```

2. **Install dependencies**
   ```bash
   pip3 install -r requirements.txt
   ```

3. **Initialize the database**
   ```bash
   python3 database/db_setup.py
   ```
   This will:
   - Create the SQLite database
   - Set up tables (users, menu, orders, order_items)
   - Seed 30+ menu items
   - Create default admin and user accounts

4. **Run the application**
   ```bash
   python3 app.py
   ```

5. **Access the application**
   Open your browser and navigate to: `http://localhost:5000`

## 🔑 Default Credentials

### Admin Account
- **Username**: `admin`
- **Password**: `admin123`
- **Access**: Full dashboard, menu management, order management, analytics

### Customer Account
- **Username**: `rahul`
- **Password**: `user123`
- **Access**: Browse menu, place orders, track orders

## 📱 User Flows

### Customer Flow
1. Sign up or login
2. Browse menu (filter by category, sort by price)
3. Add items to cart
4. View recommendations based on cart
5. Checkout (simulated payment)
6. Track order status (Kitchen → Prepared → Completed)
7. View order history

### Admin Flow
1. Login with admin credentials
2. View dashboard with analytics:
   - Total revenue, order count, average order value
   - Top selling items
   - Daily revenue trends
   - Recent orders
3. Manage menu items (Add/Edit/Delete)
4. Update order status
5. View detailed order information

## 🎯 Key Features Explained

### Pandas/NumPy Integration
- **Menu Filtering**: Uses Pandas DataFrame filtering for category and price range
- **Sorting**: DataFrame sort_values() for price and name sorting
- **Analytics**: NumPy sum(), mean() for revenue calculations
- **Aggregation**: Pandas groupby() for top-selling items
- **Time Series**: Pandas datetime operations for daily revenue

### Real-time Features
- AJAX polling for order status updates
- Live cart badge updates
- Auto-dismissing alerts

### Recommendation Engine
Simple collaborative filtering that suggests items based on:
- Top-selling items
- Items not currently in cart
- Uses NumPy for calculations

## 🔮 Future Improvements

1. **Enhanced Analytics**
   - Order heatmaps using NumPy matrices
   - Peak hour analysis
   - Customer segmentation

2. **Advanced Recommendations**
   - Collaborative filtering with co-occurrence matrix
   - Personalized recommendations based on order history

3. **Additional Features**
   - Real payment gateway integration
   - Email notifications
   - SMS alerts for order status
   - Rating and review system
   - Inventory management with low-stock alerts

4. **Performance**
   - Redis caching for menu data
   - WebSocket for real-time updates
   - Database indexing optimization

5. **UI/UX**
   - Progressive Web App (PWA)
   - Mobile app version
   - Dark mode
   - Multi-language support

## 📝 Notes

- Database is SQLite3 for simplicity (production should use PostgreSQL/MySQL)
- Payment is simulated (no real gateway integration)
- Images are placeholders (add actual food images to `static/img/`)
- Session secret key should be changed in production
- Debug mode should be disabled in production

## 🤝 Contributing

This is a demonstration project. Feel free to fork and enhance!

## 📄 License

MIT License - Free to use and modify

---

**Built with ❤️ for BMS College of Engineering**
