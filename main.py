from itertools import product
from math import prod
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from database import users, production as products

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pbase.db'
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



# @app.route("/about")
# def about():
#     return render_template("about.html", Experience=work, Education=edu)

# @app.route("/othr")
# def othr():
#     return render_template("othr.html")


# @app.route("/work/add")
# def work_add():
#     work = Work(start="2023", finish="2024", position="Web Developer")
#     db.session.add(work)
#     db.session.commit()

#     return "მონაცემი წარმატებით დაემატა"

# @app.route("/work/edit/<int:id>")
# def work_edit(id):
#     work = work.query.filter_by(id=id).first()
#     work.position = "Fullstack web dev"
#     db.session.add(work)
#     db.session.commit()
#     return "მონაცემი წარმატებით განახლდა"

# @app.route("/work/delete/<int:id>")
# def work_delete(id):
#     work = work.query.filter_by(id=id).first()
#     db.session.delete(work)
#     db.session.commit()
#     return "მონაცემი წარმატებით განახლდა"



# @app.route("/contacts")
# def contacts():
#     return "<p>Hello, contacts!</p>"

# if __name__ == "__main__":
#     app.run(debug=True)





# class Edu (db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     start = db.Column(db.String(20))
#     finish = db.Column(db.String(20), nullable=True)
#     curse = db.Column(db.String(220), nullable=False)
#     description = db.Column(db.Text)

#     def __repr__(self):
#         return '<Edu %r>' % self.curse

# class Eduform (Form):
#         start = IntegerField("კურსის დაწყება")
#         finish = IntegerField("")
#         curse = StringField("")
#         description = StringField("")


@app.before_first_request
def before_first_request():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)