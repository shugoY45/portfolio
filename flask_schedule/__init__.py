from flask import Flask
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)
app.config.from_object('flask_schedule.config')
db = SQLAlchemy(app)

# from models import Worker
from flask_schedule.views import views, login, worker, job