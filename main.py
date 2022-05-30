from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms import StringField, IntegerField, TextAreaField
app = Flask(__name__)
from database import users, production as products

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pbase.db'
app.config['SECRET_KEY'] = "super_secret_key"
db = SQLAlchemy(app)

class Product (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pname = db.Column(db.String(30))
    price = db.Column(db.Integer, nullable=True)
    trademark = db.Column(db.String(30))
    description = db.Column(db.Text)

    def __repr__(self):
        return '<Product %r>' % self.pname

class Users (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(10), nullable=False)
    
    def __repr__(self):
        return '<Users %r>' % self.email

class ProductsForm(FlaskForm):
    Product = StringField('სახელი', validators=[DataRequired()])
    Price = IntegerField('ფასი', validators=[DataRequired()])
    Trademark = StringField('მარკა', validators=[DataRequired()])
    Description = TextAreaField('აღწერა', validators=[DataRequired()])
@app.route("/")
@app.route("/home")
def main():
    products  = Product.query.all()
    return render_template("index.html", products=products)
    
def insertdata():
    for product in products:
        product = Product(pname=product.get("Product"), price=product.get("Price"), trademark=product.get("Trademark"), description=product.get("Description"))
        db.session.add (product)
        db.session.commit()
    for user in users:
        user = Users(email=user.get("email"),password=user.get("password"))
        db.session.add (user)
        db.session.commit()

@app.route("/product_add")
def addProduct():
    product = request.args
    if 'Product' in product:
        productObj = Product(
            pname       =product.get("Product"), 
            price       =product.get("Price"), 
            trademark   =product.get("Trademark"), 
            description =product.get("Description")
            )
        db.session.add (productObj)
        db.session.commit()
        return  "პროდუქტი წარმატებით დაემატა"     
    form = ProductsForm()
    return render_template("product_add.html", form=form)

@app.route("/product_edit/<int:id>")
def editProduct(id):
    product = request.args
    if 'Product' in product:
        productobj = Product.query.filter_by(id=id).first()
        db.session.add (productobj)
        db.session.commit()
        return  "პროდუქტი წარმატებით შეიცვალა"    
    form = ProductsForm()
    return render_template("product_edit.html", form=form)

@app.route("/product_delete/<int:id>")
def deleteProduct(id):
    productobj = Product.query.filter_by(id=id).first()
    db.session.delete (productobj)
    db.session.commit()
    return  "პროდუქტი წარმატებით წაიშალა"
@app.before_first_request
def before_first_request():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)