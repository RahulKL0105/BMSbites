from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3
from config import Config

auth_bp = Blueprint('auth', __name__)

def get_db_connection():
    conn = sqlite3.connect(Config.DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['role'] = user['role']
            flash('Logged in successfully!', 'success')
            if user['role'] == 'admin':
                return redirect(url_for('admin.dashboard'))
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password', 'danger')
            
    return render_template('login.html')

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form.get('confirm_password', '')
        
        # Validation
        if len(username) < 3:
            flash('Username must be at least 3 characters long.', 'danger')
            return render_template('signup.html')
        
        if len(password) < 6:
            flash('Password must be at least 6 characters long.', 'danger')
            return render_template('signup.html')
        
        if password != confirm_password:
            flash('Passwords do not match.', 'danger')
            return render_template('signup.html')
        
        conn = get_db_connection()
        try:
            # Check if username already exists
            existing_user = conn.execute('SELECT id FROM users WHERE username = ?', (username,)).fetchone()
            if existing_user:
                flash('Username already exists. Please choose a different username.', 'danger')
                return render_template('signup.html')
            
            # Create new user with role='customer'
            hashed_pw = generate_password_hash(password)
            conn.execute('INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)',
                         (username, hashed_pw, 'customer'))
            conn.commit()
            flash('Registration successful! Please login with your new account.', 'success')
            return redirect(url_for('auth.login'))
        except sqlite3.IntegrityError:
            flash('An error occurred during registration. Please try again.', 'danger')
        finally:
            conn.close()
            
    return render_template('signup.html')

@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('auth.login'))
