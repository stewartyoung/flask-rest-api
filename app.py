from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialise app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Set up database
app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dbsqlite')
app.config['SQLACLEHMY_TRACK_MODIFICATIONS'] = flask_sqlalchemy

# Initialise database
db = SQLAlchemy(app)

# Intialise Marshmallow
ma = Marshmallow(app)

# Product Class/Model
class Product(db.model):
 # primary_key=True will auto increment
 id = db.Column(db.integer, primary_key = True)
 # 100 is limit on charecters
 name = db.Column(db.String(100), unique = True)
 description = db.Column(db.String(200))
 price = db.Column(db.Float)
 qty = db.Column(db.Integer)

 def __init(self, name, description, price, qty):
  self.name = name
  self.description = description
  self.price = price
  self.qty = qty

# Run the server
if __name__ == "__main__":
 app.run()
