from datetime import datetime,time,date
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job ,Dayworker, Shift_config,SpecialJob
from flask_schedule.views.login import login_required
import make_shift


@app.route("/shift", methods=["GET", "POST"])
@login_required
@date_chosen
def shift():
  one_date = session['date']
  dayworkers = Dayworker.query.filter_by(one_date=one_date).all()
  for dayworker in dayworkers:
    dayworker.shift_init(one_date)
  jobs = Job.query.all()
  spjobs = SpecialJob.query.all()
  config = Shift_config.query.first()
  config.timecombine(one_date)
  workers , shifts = make_shift.main(dayworkers,jobs,spjobs,config)
  # print(shifts)
  return render_template("shift2.html",workers = workers,config=config)