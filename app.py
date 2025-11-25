from flask import Flask, session
from config import Config
from routes.auth import auth_bp
from routes.main import main_bp
from routes.admin import admin_bp
from routes.api import api_bp

app = Flask(__name__)
app.config.from_object(Config)

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(api_bp)

@app.context_processor
def inject_session():
    """Make session available in all templates"""
    return dict(session=session)

if __name__ == '__main__':
    print("=" * 60)
    print("🍔 BMS Bites - College Canteen Ordering System")
    print("=" * 60)
    print("\n📊 Features:")
    print("  ✓ Pandas/NumPy for menu operations & analytics")
    print("  ✓ SQLite3 database with 30+ menu items")
    print("  ✓ User authentication (Customer & Admin roles)")
    print("  ✓ Real-time order tracking")
    print("  ✓ Admin dashboard with sales analytics")
    print("  ✓ Recommendation engine")
    print("\n🔑 Default Credentials:")
    print("  Admin  - username: admin, password: admin123")
    print("  User   - username: rahul, password: user123")
    print("\n🌐 Starting server on http://127.0.0.1:5001")
    print("=" * 60)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=5001)
