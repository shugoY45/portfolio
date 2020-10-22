import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from jinja2 import *




app = Flask(__name__)
app.config.from_object('flask_schedule.config')
db = SQLAlchemy(app)

# app.jinja_env = Environment(extensions=['jinja2.ext.loopcontrols'])


# from models import Worker
from flask_schedule.views import views, login, worker, job, spjob