
from datetime import datetime,time,date,timedelta
from dateutil.relativedelta import relativedelta
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job ,Dayworker, Job,SpecialJob,Dayjob,Shift
from flask_schedule.views.login import login_required
import make_shift
from flask_schedule.forms import Selectday



@app.route("/date", methods=["GET","POST"])
@login_required
def date():
  if request.method=="POST":
    one_date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    date_select(one_date)
    
    return redirect(url_for('shift'))
  return render_template("date.html")


def date_select(one_date):
  # one_date = datetime.strptime(request.form['date'], '%Y-%m-%d')
  today = datetime.today()
  one_month_after = today + relativedelta(months=1)
  one_month_ago = today - relativedelta(months=1)
  one_week_ago = today - relativedelta(weeks=1)
  shifts = Shift.query.all()
  for shift in shifts:
    if(shift.one_date < one_week_ago ):
      db.session.delete(shift)
      db.session.commit()
  jobs = Dayjob.query.all()
  for job in jobs:
    if(job.one_date < one_week_ago ):
      db.session.delete(job)
      db.session.commit()
  workers = Dayworker.query.all()
  for worker in workers:
    if(worker.one_date < one_week_ago ):
      db.session.delete(worker)
      db.session.commit()
  if one_date > one_month_after or one_date < one_month_ago:
    flash('一ヶ月以内を選択して下さい', 'danger')
    return render_template("date.html")
  flash('日付を選択しました', 'success')
  session['date_chosen'] = True
  session['date'] = one_date
  dayworker = Dayworker.query.filter_by(one_date=one_date).all()
  if not dayworker:
    weekday = one_date.strftime('%a')
    workers = Worker.query.all()
    dayworkers = []
    if weekday == "Sun":
      for worker in workers:
        if worker.Sun:
          dayworker = Dayworker()
          dayworker.one_date = one_date
          dayworker.position = worker.position
          dayworker.workername = worker.workername
          dayworker.starttime = worker.Sunstarttime
          dayworker.endtime = worker.Sunendtime
          dayworkers.append(dayworker)
    elif weekday == "Mon":
      for worker in workers:
        if worker.Mon:
          dayworker = Dayworker()
          dayworker.one_date = one_date
          dayworker.position = worker.position
          dayworker.workername = worker.workername
          dayworker.starttime = worker.Monstarttime
          dayworker.endtime = worker.Monendtime
          dayworkers.append(dayworker)
    elif weekday == "Tue":
      for worker in workers:
        if worker.Tue:
          dayworker = Dayworker()
          dayworker.one_date = one_date
          dayworker.position = worker.position
          dayworker.workername = worker.workername
          dayworker.starttime = worker.Tuestarttime
          dayworker.endtime = worker.Tueendtime
          dayworkers.append(dayworker)
    elif weekday == "Wed":
      for worker in workers:
        if worker.Wed:
          dayworker = Dayworker()
          dayworker.one_date = one_date
          dayworker.position = worker.position
          dayworker.workername = worker.workername
          dayworker.starttime = worker.Wedstarttime
          dayworker.endtime = worker.Wedendtime
          dayworkers.append(dayworker)
    elif weekday == "Thu":
      for worker in workers:
        if worker.Thu:
          dayworker = Dayworker()
          dayworker.one_date = one_date
          dayworker.position = worker.position
          dayworker.workername = worker.workername
          dayworker.starttime = worker.Thustarttime
          dayworker.endtime = worker.Thuendtime
          dayworkers.append(dayworker)
    elif weekday == "Fri":
      for worker in workers:
        if worker.Fri:
          dayworker = Dayworker()
          dayworker.one_date = one_date
          dayworker.workername = worker.workername
          dayworker.starttime = worker.Fristarttime
          dayworker.endtime = worker.Friendtime
          dayworkers.append(dayworker)
    elif weekday == "Sat":
      for worker in workers:
        if worker.Sat:
          dayworker = Dayworker()
          dayworker.one_date = one_date
          dayworker.position = worker.position
          dayworker.workername = worker.workername
          dayworker.starttime = worker.Satstarttime
          dayworker.endtime = worker.Satendtime
          dayworkers.append(dayworker)
    db.session.add_all(dayworkers)
    db.session.commit()
  # dayworkers = Dayworker.query.filter_by(date=date).all()
  dayjob = Dayjob.query.filter_by(one_date=one_date).all()
  if not dayjob:
    jobs = Job.query.all()
    dayjobs = []
    for job in jobs:
      dayjob = Dayjob(jobname=job.jobname, one_date=one_date, starttime=job.starttime, endtime=job.endtime, priority=job.priority , required_number=job.required_number, weight=job.weight, employee_priority=job.employee_priority, parttime_priority=job.parttime_priority,helper_priority=job.helper_priority,be_indispensable=job.be_indispensable)
      dayjobs.append(dayjob)
    db.session.add_all(dayjobs)
    db.session.commit()
  
  return 0

@app.route("/dateout", methods=["GET","POST"])
@login_required
def dateout():
  session["date_chosen"] = False

  return redirect(url_for('date'))




