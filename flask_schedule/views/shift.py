from datetime import datetime,time,date
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job ,Dayworker, Shift_config,SpecialJob, Shift
from flask_schedule.forms import ShiftForm
from flask_schedule.views.login import login_required
from flask_schedule.views.views import date_chosen
import make_shift


@app.route("/shift", methods=["GET", "POST"])
@login_required
@date_chosen
def shift():
  if request.method == 'POST':
    one_date = session['date']
    dayworkers = Dayworker.query.filter_by(one_date=one_date).all()
    for dayworker in dayworkers:
      dayworker.shift_init(one_date)
    jobs = Job.query.all()
    spjobs = SpecialJob.query.all()
    config = Shift_config.query.first()
    config.timecombine(one_date)
    workers , shifts = make_shift.main(dayworkers,jobs,spjobs,config)
    for shift in shifts:
      shift.one_date = one_date
      db.session.add(shift)
      db.session.commit()
    return redirect(url_for('shiftview'))
  
  return render_template("shift2.html",workers = workers,config=config)

@app.route("/shift/new", methods=["GET", "POST"])
@login_required
@date_chosen
def new_shift():
  if request.method == 'POST':
    one_date = session['date']
    dayworkers = Dayworker.query.filter_by(one_date=one_date).all()
    for dayworker in dayworkers:
      dayworker.shift_init(one_date)
    jobs = Job.query.all()
    spjobs = SpecialJob.query.all()
    config = Shift_config.query.first()
    config.timecombine(one_date)
    shifts = make_shift.main(dayworkers,jobs,spjobs,config)
    for shift in shifts:
      shift.one_date = one_date
      db.session.add(shift)
      db.session.commit()
    return redirect(url_for('shiftview'))
  
  return render_template("shift/new.html")

@app.route("/shiftview", methods=["GET", "POST"])
@login_required
@date_chosen
def shiftview():
  one_date = session['date']
  shifts = Shift.query.filter_by(one_date=one_date).all()

  config = Shift_config.query.first()
  dayworkers = Dayworker.query.filter_by(one_date=one_date).all()
  for worker in dayworkers:
    worker.shift_init(one_date)
  for shift in shifts:
    found = False
    for worker in dayworkers:
      if shift.workername == worker.workername:
        found = True
        worker.indivshifts.append(shift)
  
  for worker in dayworkers:
    worker.indivshifts = sorted(worker.indivshifts,key=lambda x:(x.starttime))
  
  return render_template("shift/shift2.html",config=config,workers=dayworkers)


@app.route("/shift/<int:id>/edit", methods=["GET","POST"])
@login_required
@date_chosen
def edit_shift(id):
  one_date = session['date']
  shift = Shift.query.get_or_404(id)
  form = ShiftForm()
  if request.method == 'POST':
    shift.workername = form.workername.data
    shift.starttime = datetime.combine(one_date,form.starttime.data)
    shift.endtime = datetime.combine(one_date,form.endtime.data)
    db.session.commit()
    return redirect(url_for('shiftview'))
  
  workers = Dayworker.query.filter_by(one_date = one_date).all()
  worker_list = []
  for worker in workers:
    worker_list.append(worker.workername)
  form.workername.choices = worker_list
  form.workername.data = shift.workername
  form.starttime.data = shift.starttime
  form.endtime.data = shift.endtime
  return render_template("shift/edit.html",shift=shift,form=form)
  


