from flask_schedule import db


class Worker(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  workername = db.Column(db.String(20), unique=True, nullable=False)
  starttime = db.Column(db.String(10))
  endtime = db.Column(db.String(10))

  def __repr__(self):
    return f"Worker('{self.workername}', '{self.starttime}', '{self.endtime}')"