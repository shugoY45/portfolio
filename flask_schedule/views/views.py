import os
from datetime import datetime,time,date
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job ,Dayworker, Shiftconfig,Test,Job,SpecialJob,Dayjob
from flask_schedule.views.login import login_required
import make_shift
from flask_schedule.forms import Selectday, ConfigForm ,TestForm
from functools import wraps


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                 endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)

def date_chosen(view):
  @wraps(view)
  # one_date = date.min
  def inner(*args, **kwargs):
    if  session['date_chosen']:
      one_date = session['date']
    else:
      return redirect(url_for('date'))
    return view(*args, **kwargs)
  return inner

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
  
    
        
  return render_template("index.html")


@app.route("/date", methods=["GET","POST"])
@login_required
def date():
  if request.method=="POST":
    session['date_chosen'] = True
    one_date = datetime.strptime(request.form['date'], '%Y-%m-%d')
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

    return redirect(url_for('shift'))
  return render_template("date.html")

@app.route("/dateout", methods=["GET","POST"])
@login_required
def dateout():
  session["date_chosen"] = False

  return redirect(url_for('date'))




@app.route("/test", methods=["GET", "POST"])
def test():
  form = TestForm()
  config = Shiftconfig.query.first()

  a = Test()
  a.test = time(hour=11,minute=10)
  db.session.add(a)
  db.session.commit()

  test = Test.query.all()
  print(type(test[0].test))
  
  


  return render_template("test.html",form=form)
