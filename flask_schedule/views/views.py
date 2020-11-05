import os
from datetime import datetime
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job ,Dayworker
from flask_schedule.views.login import login_required
import make_shift
from flask_schedule.forms import Test, Selectday
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
  def inner(*args, **kwargs):
    if  session['date']:
      date = session['date']
    return view(*args, **kwargs)
  return inner

@app.route("/", methods=["GET", "POST"])
@login_required
def index():
  form = Selectday()
  form.weekday.choices = ["日","月","火","水","木","金","土"]
  if request.method == "POST":
    workers = Worker.query.all()
    for worker in workers:
      worker.init()
    dayworkers = []
    if form.weekday.data == "日":
      for worker in workers:
        if worker.Sunday:
          dayworkers.append(worker)
      for dayworker in dayworkers:
        dayworker.timeset(dayworker.Sunstarttime,dayworker.Sunendtime)
    elif form.weekday.data == "月":
      for worker in workers:
        if worker.Monday:
          dayworkers.append(worker)
      for dayworker in dayworkers:
        dayworker.timeset(dayworker.Monstarttime,dayworker.Monendtime)
    elif form.weekday.data == "火":
      for worker in workers:
        if worker.Tuesday:
          dayworkers.append(worker)
      for dayworker in dayworkers:
        dayworker.timeset(dayworker.Tuestarttime,dayworker.Tueendtime)
    elif form.weekday.data == "水":
      for worker in workers:
        if worker.Wednesday:
          dayworkers.append(worker)
      for dayworker in dayworkers:
        dayworker.timeset(dayworker.Wedstarttime,dayworker.Wedendtime)
    elif form.weekday.data == "木":
      for worker in workers:
        if worker.Thursday:
          dayworkers.append(worker)
      for dayworker in dayworkers:
        dayworker.timeset(dayworker.Thustarttime,dayworker.Thuendtime)
    elif form.weekday.data == "金":
      for worker in workers:
        if worker.Friday:
          dayworkers.append(worker)
      for dayworker in dayworkers:
        dayworker.timeset(dayworker.Fristarttime,dayworker.Friendtime)
    elif form.weekday.data == "土":
      for worker in workers:
        if worker.Saturday:
          dayworkers.append(worker)
      for dayworker in dayworkers:
        dayworker.timeset(dayworker.Satstarttime,dayworker.Satendtime)
    
    workers = make_shift.main(dayworkers)
    return render_template("shift.html",workers = workers)
    return redirect(url_for('shift',workers=workers))
    
        
  return render_template("index.html",form=form)

@app.route("/shift", methods=["GET", "POST"])
@login_required
@date_chosen
def shift():
  date = session['date']
  dayworkers = Dayworker.query.filter_by(date=date).all()
  workers = make_shift.main(dayworkers)
  return render_template("shift.html",workers = workers,date=date)

@app.route("/date", methods=["GET","POST"])
@login_required
def date():
  if request.method=="POST":
    session['date_chosen'] = True
    session['date'] = request.form['date']
    date = request.form['date']
    date = datetime.strptime(date, '%Y-%m-%d')
    dayworker = Dayworker.query.filter_by(date=date).all()
    if not dayworker:
      weekday = date.strftime('%a')
      workers = Worker.query.all()
      dayworkers = []
      if weekday == "Sun":
        for worker in workers:
          if worker.Sunday:
            dayworker = Dayworker()
            dayworker.date = date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Sunstarttime
            dayworker.endtime = worker.Sunendtime
            dayworkers.append(dayworker)
      elif weekday == "Mon":
        for worker in workers:
          if worker.Monday:
            dayworker = Dayworker()
            dayworker.date = date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Monstarttime
            dayworker.endtime = worker.Monendtime
            dayworkers.append(dayworker)
      elif weekday == "Tue":
        for worker in workers:
          if worker.Tuesday:
            dayworker = Dayworker()
            dayworker.date = date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Tuestarttime
            dayworker.endtime = worker.Tueendtime
            dayworkers.append(dayworker)
      elif weekday == "Wed":
        for worker in workers:
          if worker.Wednesday:
            dayworker = Dayworker()
            dayworker.date = date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Wedstarttime
            dayworker.endtime = worker.Wedendtime
            dayworkers.append(dayworker)
      elif weekday == "Thu":
        for worker in workers:
          if worker.Thursday:
            dayworker = Dayworker()
            dayworker.date = date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Thustarttime
            dayworker.endtime = worker.Thuendtime
            dayworkers.append(dayworker)
      elif weekday == "Fri":
        for worker in workers:
          if worker.Friday:
            dayworker = Dayworker()
            dayworker.date = date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Fristarttime
            dayworker.endtime = worker.Friendtime
            dayworkers.append(dayworker)
      elif weekday == "Sat":
        for worker in workers:
          if worker.Saturday:
            dayworker = Dayworker()
            dayworker.date = date
            dayworker.workername = worker.workername
            dayworker.starttime = worker.Satstarttime
            dayworker.endtime = worker.Satendtime
            dayworkers.append(dayworker)
      db.session.add_all(dayworkers)
      db.session.commit()
    dayworkers = Dayworker.query.filter_by(date=date).all()
    return redirect(url_for('shift'))
  return render_template("date.html")

@app.route("/test", methods=["GET", "POST"])
def test():
  date = session['date']
  date = datetime.strptime(date, '%Y-%m-%d')
  # print(date)
  dayworker = Dayworker.query.filter_by(date=date).all()
  if dayworker:
    print(1)
  else :
    print(2)
  return render_template("test.html")



