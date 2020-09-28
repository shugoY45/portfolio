from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config['SECRET_KEY'] = '5bdc41204800aae4cacd107625b60bfc'
app.config['SQLALCHEMY_DATEBASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flask_schedule import routes