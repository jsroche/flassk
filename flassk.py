from flask import Flask, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_DBNAME'] = "0802d52fe345cc6838bea8291ed4b275f4b42a20"
mongo = PyMongo(app)

@app.route('/')
def home():
    return 'This is the landing page that needs some work'

@app.route('/admin')
def admin():
    return "probably don't need this"

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/hello/<name>')
def hello_name(name):
   if name == 'jim' or 'admin':
       return redirect(url_for('admin'))
   else:
       return 'Hello %s!' % name

@app.route('/sav_summary')
def sav_summary():
   return 'Welcome to the SAV summary page'

@app.route('/production_summary')
def prod_summary():
   return 'Welcome to the Production summary page'

if __name__ == '__main__':
    app.run(debug=True)
