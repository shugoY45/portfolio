from flask_script import Manager
from flask_schedule import app
from flask_schedule.scripts.db import InitDB,DeleteDB

if __name__ == "__main__":
  manager = Manager(app)
  manager.add_command('init_db', InitDB())
  manager.add_command('delete_db',DeleteDB())
  manager.run()