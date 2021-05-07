from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

#                                                              superuser/password         |db name     
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:Glory27!@localhost/crud'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://bxoalbgxqdjkvv:fc27ec318e7348544224e15c64ce66f43cd5be6011b342212d86037fc319d3d1@ec2-54-224-194-214.compute-1.amazonaws.com:5432/d16vlromcp4o0v'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  #uses a lot of cpu.


#Create an instance of SQLAlchemy
db = SQLAlchemy(app)

# DB Model from which the tables will be created
class Favquotes(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(2000))


@app.route('/')
def index():
    # store all db data in a table variable, and the variable renders on index page.
    result = Favquotes.query.all()
    return render_template('index.html', result=result)


@app.route('/quotes')
def quotes():
    return render_template('quotes.html')


@app.route('/process', methods=['POST'])
def process():
    # Always store form data in variables first
    author = request.form['author']
    quote = request.form['quote']
    quotedata =Favquotes(author=author, quote=quote) # Then store those variables into your table variable
    db.session.add(quotedata)  # Then add that data to the database
    db.session.commit() # Commit the data in the database

    return redirect(url_for('index')) # note for POST, the extension must not be used; this is the View function


if __name__=='__main__':
    app.run(debug=True)