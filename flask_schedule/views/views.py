import os
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Worker ,Job
from flask_schedule.views.login import login_required
import make_shift
from flask_schedule.forms import Test, Selectday


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
    
    workers = dayworkers
    make_shift.main()
    return render_template("shift.html",workers = workers)
    
        
  return render_template("index.html",form=form)

@app.route("/shift", methods=["GET", "POST"])
@login_required
def shift():
  workers = dayworkers
  make_shift.main()
  return render_template("shift.html",workers = workers)


@app.route("/test", methods=["GET", "POST"])
def test():
  workers = Worker.query.all()
  # make_shift.main()
  forms = []
  for _ in range(3):
    forms.append(Test())
  if request.method=="POST":
    for form in forms:
      print(form.name)

  return render_template("test.html",workers = workers,forms=forms)



