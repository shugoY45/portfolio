import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from jinja2 import *




app = Flask(__name__)
app.config.from_object('flask_schedule.config')
db_uri = "sqlite:///" + os.path.join(app.root_path, 'site.db') or "postgres://obwkcqkdnweeeq:57b1214817ae4efd7be6b26bed59a6835df968882f615aca9141fe7848f8ce6d@ec2-54-157-234-29.compute-1.amazonaws.com:5432/d12kknduts3889"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)

# app.jinja_env = Environment(extensions=['jinja2.ext.loopcontrols'])


# from models import Worker
from flask_schedule.views import views, login, worker, job, spjob