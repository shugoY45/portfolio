import os
from datetime import datetime,time,date
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job ,Dayworker, Shift_config,Test,Job,SpecialJob
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
  
    
        
  return render_template("index.html",form=form)

@app.route("/shift", methods=["GET", "POST"])
@login_required
@date_chosen
def shift():
  one_date = session['date']
  dayworkers = Dayworker.query.filter_by(one_date=one_date).all()
  jobs = Job.query.all()
  spjobs = SpecialJob.query.all()
  config = Shift_config.query.first()
  config.timecombine(one_date)
  workers = make_shift.main(dayworkers,jobs,spjobs,config)
  return render_template("shift.html",workers = workers,date=one_date)

@app.route("/date", methods=["GET","POST"])
@login_required
def date():
  if request.method=="POST":
    session['date_chosen'] = True
    one_date = datetime.strptime(request.form['date'], '%Y-%m-%d')
    session['date'] = one_date
    print(type(one_date))
    # date = datetime.strptime(date, '%Y/%m/%d (%A)')
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
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Sunstarttime
            dayworker.endtime = worker.Sunendtime
            dayworkers.append(dayworker)
      elif weekday == "Mon":
        for worker in workers:
          if worker.Mon:
            dayworker = Dayworker()
            dayworker.one_date = one_date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Monstarttime
            dayworker.endtime = worker.Monendtime
            dayworkers.append(dayworker)
      elif weekday == "Tue":
        for worker in workers:
          if worker.Tue:
            dayworker = Dayworker()
            dayworker.one_date = one_date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Tuestarttime
            dayworker.endtime = worker.Tueendtime
            dayworkers.append(dayworker)
      elif weekday == "Wed":
        for worker in workers:
          if worker.Wed:
            dayworker = Dayworker()
            dayworker.one_date = one_date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Wedstarttime
            dayworker.endtime = worker.Wedendtime
            dayworkers.append(dayworker)
      elif weekday == "Thu":
        for worker in workers:
          if worker.Thu:
            dayworker = Dayworker()
            dayworker.one_date = one_date
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
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Satstarttime
            dayworker.endtime = worker.Satendtime
            dayworkers.append(dayworker)
      db.session.add_all(dayworkers)
      db.session.commit()
    # dayworkers = Dayworker.query.filter_by(date=date).all()
    # return redirect(url_for('shift'))
  return render_template("date.html")

@app.route("/dateout", methods=["GET","POST"])
@login_required
def dateout():
  session["date_chosen"] = False

  return redirect(url_for('date'))

@app.route("/normal_config", methods=["GET", "POST"])
def normal_config():
  form = ConfigForm()
  if not Shift_config.query.first():
    if request.method == 'GET':
      return render_template("normal_config.html",form=form)
    if request.method == 'POST':
      config=Shift_config()
      config.store_opentime=form.store_opentime.data
      config.store_closetime=form.store_closetime.data
      config.resttime=form.resttime.data
      config.restnd_mint=form.restnd_mint.data
      config.restname=form.restname.data
      config.priorty_max=form.priorty_max.data
      config.min_shift=form.min_shift.data
      config.job_divtime=form.job_divtime.data
      db.session.add(config)
      db.session.commit()
  else:
    config = Shift_config.query.first()
    print(config.store_opentime)
    if request.method == 'GET':
      form.store_opentime.data=config.store_opentime
      form.store_closetime.data=config.store_closetime
      form.resttime.data=config.resttime
      form.restnd_mint.data=config.restnd_mint
      form.restname.data=config.restname
      form.priorty_max.data=config.priorty_max
      form.min_shift.data=config.min_shift
      form.job_divtime.data=config.job_divtime
      return render_template("normal_config.html",form=form)
    if request.method == 'POST':
      config.store_opentime=form.store_opentime.data
      config.store_closetime=form.store_closetime.data
      config.resttime=form.resttime.data
      config.restnd_mint=form.restnd_mint.data
      config.restname=form.restname.data
      config.priorty_max=form.priorty_max.data
      config.min_shift=form.min_shift.data
      config.job_divtime=form.job_divtime.data
      db.session.commit()


  return render_template("normal_config.html",form=form)


@app.route("/test", methods=["GET", "POST"])
def test():
  form = TestForm()
  config = Shift_config.query.first()

  a = Test()
  a.test = time(hour=11,minute=10)
  db.session.add(a)
  db.session.commit()

  test = Test.query.all()
  print(type(test[0].test))
  
  


  return render_template("test.html",form=form)
