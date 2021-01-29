from datetime import datetime,time,date
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job ,Dayworker, Shiftconfig,SpecialJob, Shift,Dayjob
from flask_schedule.forms import ShiftForm
from flask_schedule.views.login import login_required
from flask_schedule.views.views import date_chosen
import make_shift


@app.route("/shift", methods=["GET", "POST"])
@login_required
@date_chosen
def shift():
  one_date = session['date']
  shifts = Shift.query.filter_by(one_date=one_date).all()

  config = Shiftconfig.query.first()
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
  
  return render_template("shift/shift.html",config=config,workers=dayworkers)

@app.route("/shift/new", methods=["GET", "POST"])
@login_required
@date_chosen
def new_shift():
  if request.method == 'POST':
    one_date = session['date']
    preshifts = Shift.query.filter_by(one_date=one_date).all()
    if preshifts:
      for shift in preshifts:
        db.session.delete(shift)
      db.session.commit()
      
    dayworkers = Dayworker.query.filter_by(one_date=one_date).all()
    for dayworker in dayworkers:
      dayworker.shift_init(one_date)
    jobs = Dayjob.query.filter_by(one_date=one_date).all()
    spjobs = SpecialJob.query.all()
    config = Shiftconfig.query.first()
    config.timecombine(one_date)
    shifts = make_shift.main(dayworkers,jobs,spjobs,config)
    for shift in shifts:
      shift.one_date = one_date
      db.session.add(shift)
      db.session.commit()
    return redirect(url_for('shift'))
  
  return render_template("shift/new.html")

# @app.route("/shift", methods=["GET", "POST"])
# @login_required
# @date_chosen
# def shift():
#   one_date = session['date']
#   shifts = Shift.query.filter_by(one_date=one_date).all()

#   config = Shiftconfig.query.first()
#   dayworkers = Dayworker.query.filter_by(one_date=one_date).all()
#   for worker in dayworkers:
#     worker.shift_init(one_date)
#   for shift in shifts:
#     found = False
#     for worker in dayworkers:
#       if shift.workername == worker.workername:
#         found = True
#         worker.indivshifts.append(shift)
  
#   for worker in dayworkers:
#     worker.indivshifts = sorted(worker.indivshifts,key=lambda x:(x.starttime))
  
#   return render_template("shift/shift.html",config=config,workers=dayworkers)


@app.route("/shift/<int:id>/edit", methods=["GET","POST"])
@login_required
@date_chosen
def edit_shift(id):
  one_date = session['date']
  shift = Shift.query.get_or_404(id)
  workers = Dayworker.query.filter_by(one_date = one_date).all()
  return render_template("shift/edit.html",shift=shift)
  
@app.route("/shift/<int:id>/changeworker", methods=["GET","POST"])
@login_required
@date_chosen
def change_worker(id):
  one_date = session['date']
  shift = Shift.query.get_or_404(id)
  form = ShiftForm()
  if request.method == 'POST':
    
    flash('変更しました',"success")
    shift.workername = form.workername.data
    db.session.commit()
    return redirect(url_for('shift'))

  
  workers = Dayworker.query.filter_by(one_date = one_date).all()
  worker_list = []
  flash('従業員を変更します',"warning")
  for worker in workers:
    worker_list.append(worker.workername)
  form.workername.choices = worker_list
  form.workername.data = shift.workername
  return render_template("shift/changeworker.html",shift=shift,form=form)

