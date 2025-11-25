# Technical Documentation - BMS Bites

This document provides a comprehensive breakdown of all technical implementations in the BMS Bites project, specifically focusing on SQLite3, Pandas, NumPy, and Python functions usage.

## 📚 Table of Contents
1. [SQLite3 Usage](#sqlite3-usage)
2. [Pandas Usage](#pandas-usage)
3. [NumPy Usage](#numpy-usage)
4. [Python Standard Library Functions](#python-standard-library-functions)
5. [Flask Framework Functions](#flask-framework-functions)
6. [Data Flow Architecture](#data-flow-architecture)

---

## 🗄️ SQLite3 Usage

### Database Connection Pattern

**Used in**: All `utils/*.py` files

```python
import sqlite3
conn = sqlite3.connect(Config.DATABASE)
cursor = conn.cursor()
# ... operations ...
conn.commit()
conn.close()
```

### File-by-File Breakdown

#### 1. `database/db_setup.py`

**Line 9-11**: Database initialization
```python
conn = sqlite3.connect(DB_PATH)
with open(SCHEMA_PATH, 'r') as f:
    conn.executescript(f.read())  # Execute entire schema
```

**Line 16-18**: Insert with parameterized query (prevents SQL injection)
```python
cursor.execute("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)",
               ('admin', admin_pass, 'admin'))
```

**Line 32**: Bulk insert using executemany
```python
cursor.executemany("INSERT INTO canteens (...) VALUES (?, ?, ?, ?, ?, ?)", canteens)
```

**Line 90**: Bulk menu insert
```python
cursor.executemany("INSERT INTO menu (...) VALUES (?, ?, ?, ?, ?, ?)", all_items)
```

#### 2. `utils/menu_manager.py`

**Lines 11-14**: SELECT query with Pandas integration
```python
conn = sqlite3.connect(self.db_path)
df = pd.read_sql_query("SELECT * FROM canteens WHERE is_open=1", conn)
conn.close()
```

**Lines 28-33**: Conditional SELECT with parameter
```python
if canteen_id:
    df = pd.read_sql_query("SELECT * FROM menu WHERE canteen_id=?", 
                           conn, params=(canteen_id,))
```

**Lines 64-67**: UPDATE query
```python
cursor.execute("""
    UPDATE menu 
    SET canteen_id=?, name=?, description=?, price=?, category=?, image_url=?, is_available=?
    WHERE id=?
""", (canteen_id, name, description, price, category, image_url, is_available, item_id))
```

**Lines 72-75**: DELETE query
```python
cursor.execute("DELETE FROM menu WHERE id=?", (item_id,))
```

#### 3. `utils/order_manager.py`

**Lines 15-17**: INSERT with AUTOINCREMENT and lastrowid
```python
cursor.execute("INSERT INTO orders (user_id, canteen_id, total_amount, status) VALUES (?, ?, ?, ?)",
               (user_id, canteen_id, total_amount, 'kitchen'))
order_id = cursor.lastrowid  # Get auto-generated ID
```

**Lines 20-22**: INSERT in loop for order items
```python
for item in cart_items:
    cursor.execute("INSERT INTO order_items (...) VALUES (?, ?, ?, ?)",
                   (order_id, item['menu_id'], item['quantity'], item['price']))
```

**Lines 33-35**: SELECT with ORDER BY
```python
orders = pd.read_sql_query("SELECT * FROM orders WHERE user_id=? ORDER BY created_at DESC", 
                           conn, params=(user_id,))
```

**Lines 41-46**: JOIN query
```python
items = pd.read_sql_query("""
    SELECT oi.*, m.name, m.image_url 
    FROM order_items oi 
    JOIN menu m ON oi.menu_id = m.id 
    WHERE oi.order_id=?
""", conn, params=(order_id,))
```

**Lines 68-73**: Multi-table JOIN
```python
orders = pd.read_sql_query("""
    SELECT o.*, u.username, c.name as canteen_name
    FROM orders o 
    JOIN users u ON o.user_id = u.id 
    JOIN canteens c ON o.canteen_id = c.id
    ORDER BY o.created_at DESC
""", conn)
```

**Lines 59-62**: UPDATE query
```python
cursor.execute("UPDATE orders SET status=? WHERE id=?", (status, order_id))
```

#### 4. `utils/analytics.py`

**Lines 11-14**: Simple SELECT
```python
conn = sqlite3.connect(self.db_path)
df = pd.read_sql_query("SELECT * FROM orders", conn)
conn.close()
```

### SQLite3 Functions Used

| Function | Purpose | Location |
|----------|---------|----------|
| `sqlite3.connect()` | Create database connection | All utils files |
| `cursor.execute()` | Execute single SQL statement | INSERT, UPDATE, DELETE operations |
| `cursor.executemany()` | Execute statement multiple times | Bulk inserts in db_setup.py |
| `cursor.executescript()` | Execute SQL script | Schema initialization |
| `cursor.lastrowid` | Get last inserted row ID | Order creation |
| `conn.commit()` | Save changes | After all modifications |
| `conn.close()` | Close connection | End of all operations |
| `conn.row_factory` | Set row return format | routes/auth.py line 11 |

---

## 🐼 Pandas Usage

### Core Pandas Functions

#### 1. `pd.read_sql_query()`

**Purpose**: Convert SQL query results directly to DataFrame

**Locations**:
- `utils/menu_manager.py`: Lines 12, 18, 29, 81
- `utils/order_manager.py`: Lines 33, 40, 42, 68
- `utils/analytics.py`: Lines 12, 18, 24

**Example**:
```python
df = pd.read_sql_query("SELECT * FROM menu", conn)
# Returns: DataFrame with columns matching table schema
```

**Why Pandas?** Enables powerful data manipulation that would require complex SQL

#### 2. DataFrame Filtering

**File**: `utils/menu_manager.py`

**Lines 38-40**: Boolean indexing
```python
df = df[df['is_available'] == 1]  # Filter available items
```

**Lines 43-44**: Category filter
```python
if category and category != 'all':
    df = df[df['category'] == category]
```

**Lines 47-48**: Price range filter (NumPy-style boolean indexing)
```python
df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]
```

**Why Pandas?** Much cleaner than SQL WHERE clauses for multiple conditions

#### 3. DataFrame Sorting

**File**: `utils/menu_manager.py`

**Lines 51-56**: Conditional sorting
```python
if sort_by == 'price_asc':
    df = df.sort_values(by='price', ascending=True)
elif sort_by == 'price_desc':
    df = df.sort_values(by='price', ascending=False)
else:
    df = df.sort_values(by='name')
```

**Why Pandas?** Dynamic sorting based on user selection

#### 4. DataFrame Aggregation

**File**: `utils/analytics.py`

**Lines 52-56**: GroupBy and aggregation
```python
merged = pd.merge(items, menu, left_on='menu_id', right_on='id')
top_items = merged.groupby('name')['quantity'].sum().sort_values(ascending=False).head(n)
```

**Breakdown**:
- `pd.merge()`: JOIN two DataFrames
- `.groupby('name')`: Group by item name
- `['quantity'].sum()`: Sum quantities per group
- `.sort_values(ascending=False)`: Sort descending
- `.head(n)`: Get top N items

**Why Pandas?** Equivalent SQL would be complex GROUP BY with JOIN

#### 5. DateTime Operations

**File**: `utils/analytics.py`

**Lines 66-67**: Date parsing and grouping
```python
orders['created_at'] = pd.to_datetime(orders['created_at'])
daily = orders.groupby(orders['created_at'].dt.date)['total_amount'].sum()
```

**Breakdown**:
- `pd.to_datetime()`: Convert string to datetime
- `.dt.date`: Extract date component
- `.groupby()`: Group by date
- `.sum()`: Sum revenue per day

**Why Pandas?** Time-series analysis made simple

#### 6. DataFrame Conversion

**Lines throughout**: `.to_dict('records')`
```python
return df.to_dict('records')
# Converts DataFrame to list of dictionaries for JSON/templates
```

**Line 58**: `.to_dict()` (Series to dict)
```python
return top_items.to_dict()
```

**Why Pandas?** Easy conversion between formats

#### 7. DataFrame Sampling

**File**: `utils/analytics.py`

**Lines 81-83**: Random sampling
```python
sample = menu[menu['is_available'] == 1].sample(min(3, len(menu)))
return sample.to_dict('records')
```

**Why Pandas?** Built-in random sampling for recommendations

#### 8. DataFrame Properties

**Lines throughout**:
- `.empty`: Check if DataFrame has no rows
- `.iloc[0]`: Get first row
- `.to_dict()`: Convert row to dictionary

### Pandas Functions Summary

| Function | Purpose | File | Lines |
|----------|---------|------|-------|
| `pd.read_sql_query()` | SQL to DataFrame | menu_manager.py, order_manager.py, analytics.py | Multiple |
| `df[condition]` | Boolean filtering | menu_manager.py | 38, 43, 47 |
| `df.sort_values()` | Sorting | menu_manager.py | 51-56 |
| `pd.merge()` | JOIN DataFrames | analytics.py | 53 |
| `.groupby()` | Aggregation | analytics.py | 56, 67 |
| `pd.to_datetime()` | Date parsing | analytics.py | 66 |
| `.dt.date` | Extract date | analytics.py | 67 |
| `.to_dict()` | Convert to dict | All utils | Multiple |
| `.sample()` | Random sampling | analytics.py | 82 |
| `.empty` | Check if empty | All utils | Multiple |
| `.iloc[]` | Position-based indexing | All utils | Multiple |
| `.head()` | Get first N rows | analytics.py | 56 |

---

## 🔢 NumPy Usage

### Core NumPy Functions

#### 1. `np.sum()`

**File**: `utils/analytics.py`

**Line 34**: Calculate total revenue
```python
total_revenue = np.sum(orders['total_amount'])
```

**Why NumPy?** Faster than Python's built-in `sum()` for large datasets

#### 2. `np.mean()`

**File**: `utils/analytics.py`

**Line 36**: Calculate average order value
```python
avg_order_value = np.mean(orders['total_amount'])
```

**Why NumPy?** Handles NaN values better, more efficient

#### 3. Boolean Indexing (NumPy-style in Pandas)

**File**: `utils/menu_manager.py`

**Line 47-48**: Combined conditions
```python
df = df[(df['price'] >= min_price) & (df['price'] <= max_price)]
```

**Note**: Pandas uses NumPy's boolean indexing under the hood

### NumPy Functions Summary

| Function | Purpose | File | Line |
|----------|---------|------|------|
| `np.sum()` | Sum array elements | analytics.py | 34 |
| `np.mean()` | Calculate mean | analytics.py | 36 |
| Boolean `&` | AND operation | menu_manager.py | 47 |

### Why NumPy?

1. **Performance**: 10-100x faster than Python loops
2. **Vectorization**: Operations on entire arrays
3. **Memory Efficiency**: Optimized C implementation
4. **Integration**: Works seamlessly with Pandas

---

## 🐍 Python Standard Library Functions

### 1. `os` Module

**File**: `database/db_setup.py`

**Lines 5-6**: Path operations
```python
DB_PATH = os.path.join(os.path.dirname(__file__), 'bmsbites.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')
```

**Functions**:
- `os.path.join()`: Platform-independent path joining
- `os.path.dirname()`: Get directory name
- `__file__`: Current file path

**File**: `config.py`

**Lines 4-5**:
```python
DATABASE = os.path.join(os.getcwd(), 'database', 'bmsbites.db')
UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'img')
```

**Functions**:
- `os.getcwd()`: Get current working directory

### 2. `werkzeug.security`

**File**: `database/db_setup.py`

**Lines 16, 21**: Password hashing
```python
from werkzeug.security import generate_password_hash
admin_pass = generate_password_hash('admin123')
```

**File**: `routes/auth.py`

**Lines 1, 20, 33**: Password verification
```python
from werkzeug.security import check_password_hash
if user and check_password_hash(user['password_hash'], password):
```

**Functions**:
- `generate_password_hash()`: Create secure password hash
- `check_password_hash()`: Verify password

### 3. `functools`

**File**: `routes/admin.py`

**Lines 5, 13**: Decorator preservation
```python
import functools

@functools.wraps(view)
def wrapped_view(**kwargs):
    # ...
```

**Purpose**: Preserve function metadata when creating decorators

### 4. Built-in Functions

**Throughout codebase**:

```python
# Type conversions
int(request.form['canteen_id'])  # String to integer
float(request.form['price'])      # String to float
str(item_id)                      # Integer to string

# Collections
len(orders)                       # Length of list
sum(item['price'] * item['quantity'] for item in cart_items)  # Sum with generator
list(cart_ids.keys())            # Dict keys to list
dict(session=session)            # Create dictionary

# Iteration
for item_id, qty in cart_ids.items():  # Iterate dict
for item in menu_items:                # Iterate list

# Conditionals
if not cart_ids:                  # Check if empty
if 'user_id' in session:         # Check membership

# String operations
f"Order #{order_id}"             # F-string formatting
'success' if condition else 'danger'  # Ternary operator
```

---

## 🌶️ Flask Framework Functions

### 1. Routing Decorators

```python
@main_bp.route('/')
@main_bp.route('/menu')
@main_bp.route('/add_to_cart/<int:item_id>', methods=['POST'])
```

### 2. Request Handling

**File**: `routes/main.py`

```python
from flask import request

request.args.get('category', 'all')  # GET parameters
request.form['name']                  # POST form data
request.method                        # HTTP method
```

### 3. Response Functions

```python
from flask import render_template, redirect, url_for, flash, jsonify

render_template('menu.html', menu_items=items)  # Render HTML
redirect(url_for('main.menu'))                  # Redirect to route
flash('Message', 'success')                     # Flash message
jsonify({'status': 'success'})                  # JSON response
```

### 4. Session Management

```python
from flask import session

session['user_id'] = user['id']     # Set session variable
session.get('cart', {})              # Get with default
session.modified = True              # Mark as modified
session.clear()                      # Clear all
```

### 5. Blueprints

```python
from flask import Blueprint

main_bp = Blueprint('main', __name__)
admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

app.register_blueprint(main_bp)
```

---

## 🏗️ Data Flow Architecture

### Request Flow Example: Ordering Food

```
1. User clicks "Add to Cart"
   ↓
2. POST /add_to_cart/5 (routes/main.py)
   ↓
3. session['cart'][5] = quantity
   ↓
4. Redirect to /cart
   ↓
5. GET /cart (routes/main.py)
   ↓
6. menu_mgr.get_item(5) (utils/menu_manager.py)
   ↓
7. SQLite: SELECT * FROM menu WHERE id=5
   ↓
8. Pandas: df.iloc[0].to_dict()
   ↓
9. Return item data
   ↓
10. Render cart.html with items
```

### Analytics Flow Example: Top Selling Items

```
1. Admin visits /admin/dashboard
   ↓
2. analytics_mgr.get_top_selling_items() (utils/analytics.py)
   ↓
3. SQLite: SELECT * FROM order_items
   ↓
4. Pandas: pd.read_sql_query() → DataFrame
   ↓
5. SQLite: SELECT * FROM menu
   ↓
6. Pandas: pd.merge(items, menu)
   ↓
7. Pandas: .groupby('name')['quantity'].sum()
   ↓
8. Pandas: .sort_values(ascending=False)
   ↓
9. Pandas: .head(5)
   ↓
10. Pandas: .to_dict()
   ↓
11. Return top 5 items
   ↓
12. Render dashboard.html
```

---

## 📊 Technology Stack Summary

| Technology | Usage | Files |
|------------|-------|-------|
| **SQLite3** | Database operations | All utils/, db_setup.py, routes/auth.py |
| **Pandas** | Data manipulation, SQL integration | All utils/ files |
| **NumPy** | Numerical calculations | utils/analytics.py |
| **Flask** | Web framework | app.py, all routes/ |
| **Werkzeug** | Password hashing | db_setup.py, routes/auth.py |
| **Jinja2** | Template engine | All templates/ |
| **Bootstrap** | CSS framework | All templates/ |

---

## 🎯 Key Design Patterns

### 1. Manager Pattern
- `MenuManager`, `OrderManager`, `AnalyticsManager`
- Encapsulates database operations
- Reusable across routes

### 2. Blueprint Pattern
- Modular route organization
- `auth_bp`, `main_bp`, `admin_bp`, `api_bp`

### 3. Decorator Pattern
- `@admin_required` for authorization
- `@functools.wraps` for metadata preservation

### 4. Session Pattern
- User authentication
- Shopping cart persistence

---

## 📈 Performance Considerations

### Why Pandas Over Raw SQL?

1. **Complex Filtering**: Multiple conditions easier in Pandas
2. **Data Transformation**: Built-in functions for common operations
3. **Flexibility**: Easy to add new filters without SQL changes
4. **Type Safety**: Automatic type handling

### Why NumPy?

1. **Speed**: C-optimized operations
2. **Vectorization**: Operate on entire arrays
3. **Memory**: Efficient storage

### Trade-offs

- **Small datasets**: Pandas overhead not significant
- **Large datasets**: Pandas/NumPy shine
- **Complex queries**: SQL might be more efficient
- **Simple CRUD**: Direct SQL is fine

---

## 🔍 Code Quality Features

1. **Parameterized Queries**: Prevents SQL injection
2. **Password Hashing**: Secure authentication
3. **Session Management**: Stateful user experience
4. **Error Handling**: Graceful fallbacks
5. **Modular Design**: Easy to maintain and extend

---

**For user modifications, see `rahuk.md`**
**For general information, see `README.md`**
