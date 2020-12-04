import os
from datetime import datetime,time,date,timedelta
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Test
from flask_schedule.views.login import login_required
from flask_schedule.forms import TestForm
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
