from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Initialise app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# Set up database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'dbsqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialise database
db = SQLAlchemy(app)

# Intialise Marshmallow
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
 # primary_key=True will auto increment
 id = db.Column(db.Integer, primary_key = True)
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

# Product Schema
class ProductSchema(ma.Schema):
 class Meta:
  fields = ('id', 'name', 'description', 'price', 'qty')

# intialise schema
product_schema = ProductSchema(strict=True)
products_schema = ProductSchema(many=True, strict=True)

# Create a product_schema
@app.route('/product', methods=['post'])
def add_product():
 name = request.json['name']
 description = request.json['name']
 price = request.json['name']
 qty = request.json['name']

 new_product = Prodcut(name, description, price, qty)

 db.session.add(new_product)
 db.session.commit()

 return product_schema.jsonify(new_product)

# Run the server
if __name__ == "__main__":
 app.run()
