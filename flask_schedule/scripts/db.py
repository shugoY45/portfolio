from flask_script import Command
from flask_schedule import db

class InitDB(Command):
  "create database"

  def run(self):
    db.create_all()

class DeleteDB(Command):

  def run(self):
    db.drop_all()