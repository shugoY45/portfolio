from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job
import make_shift


@app.route("/", methods=["GET", "POST"])
def index():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  workers = Worker.query.all()
  jobs = Job.query.all()
  make_shift.main()
  return render_template("index.html")




