#!/usr/bin/env python3
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from server.app import app, db
from server.models import Restaurant, Pizza, RestaurantPizza

with app.app_context():
    # Create all tables
    db.create_all()
    print("Database tables created successfully!")
