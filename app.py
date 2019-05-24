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

 def __init__(self, name, description, price, qty):
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

# Create a post product route
@app.route('/product', methods=['POST'])
def add_product():
 name = request.json['name']
 description = request.json['description']
 price = request.json['price']
 qty = request.json['qty']

 new_product = Product(name, description, price, qty)

 db.session.add(new_product)
 db.session.commit()

 return product_schema.jsonify(new_product)

# Create a get all products route
@app.route('/product', methods=['GET'])
def get_products():
 all_products = Product.query.all()
 result = products_schema.dump(all_products)
 return jsonify(result.data)

# Create a get single product route
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
 product = Product.query.get(id)
 return product_schema.jsonify(product)

# Update a product on a route
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
 product = Product.query.get(id)

 name = request.json['name']
 description = request.json['description']
 price = request.json['price']
 qty = request.json['qty']

 product.name = name
 product.description = description
 product.price = price
 product.qty = qty

 db.session.commit()

 return product_schema.jsonify(product)

 # Delete a product route
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
 product = Product.query.get(id)
 db.session.delete(product)
 db.session.commit()
 
 return product_schema.jsonify(product)


# Run the server
if __name__ == "__main__":
 app.run()
