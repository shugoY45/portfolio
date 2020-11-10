import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate





app = Flask(__name__)
app.config.from_object('flask_schedule.config')
db_uri = os.environ.get('DATABASE_URL') or 'postgresql+psycopg2://{user}:{password}@{host}/{name}'.format(**{
    'user': 'shugo',
    'password': 'ys45',
    'host': 'localhost',
    'name': 'db.postgresql'
}) or "sqlite:///" + os.path.join(app.root_path, 'site.db')
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)
migrate = Migrate(app,db)



# from models import Worker
from flask_schedule.views import views, login, worker, job, spjob,dayworker