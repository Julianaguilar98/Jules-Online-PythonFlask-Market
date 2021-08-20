from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SECRET_KEY'] = '557982242aadc2f48524c3e6'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from market import routes