from datetime import datetime,time,date
from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.models import Shiftconfig, Position
from flask_schedule.views.login import login_required
from flask_schedule.forms import ConfigForm 


@app.route("/normal_config", methods=["GET", "POST"])
def normal_config():
  form = ConfigForm()
  if not Shiftconfig.query.first():
    if request.method == 'GET':
      return render_template("normal_config.html",form=form)
    if request.method == 'POST':
      config=Shiftconfig()
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
    config = Shiftconfig.query.first()
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

@app.route("/normal_config", methods=["GET", "POST"])
def add_position():
  position = Position.query.all()