from flask import Flask
from models import db
from config import Config

def test_connection():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        try:
            # Test connection
            db.engine.execute('SELECT 1')
            print("✅ Database connection successful!")

            # Create tables
            db.create_all()
            print("✅ Tables created successfully!")

            # Check if tables exist
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            print(f"📋 Tables in database: {tables}")

            return True
        except Exception as e:
            print(f"❌ Database error: {e}")
            return False

if __name__ == "__main__":
    test_connection()
