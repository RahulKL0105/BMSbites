import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-prod'
    DATABASE = os.path.join(os.getcwd(), 'database', 'bmsbites.db')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'static', 'img')
