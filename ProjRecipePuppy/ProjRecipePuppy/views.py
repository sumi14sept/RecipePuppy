"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ProjRecipePuppy import app
import sqlite3
from flask import g

DATABASE = "C:\\Myworkspace\\proj_RecipePuppy\\dbRecipes.db" #path for the database

# get database object
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
@app.route('/home')
def home():
    try:
        x = int(input("Please enter a number: "))
        
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

    try:
        cur = get_db().execute("SELECT * FROM tblRecipePuppy")
        datalist = cur.fetchall()
    except Exception as e:
        return (str(e))
    cur.close()
    return render_template('index.html',title='Home Page',datalist=datalist)


