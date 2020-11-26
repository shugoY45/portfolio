from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import JobForm
from flask_schedule.models import Dayjob, Shiftconfig
from flask_schedule.views.login import login_required
from flask_schedule.views.views import date_chosen


@app.route('/dayjob', methods=['GET', 'POST'])
@login_required
@date_chosen
def dayjob():
  one_date = session['date']
  jobs = Dayjob.query.filter_by(one_date=one_date).all()
  return render_template('dayjob/dayjob.html',jobs=jobs)

@app.route('/dayjob/new', methods=['GET', 'POST'])
@login_required
@date_chosen
def new_dayjob():
  one_date = session['date']
  strdate = one_date.strftime('%Y/%m/%d (%a)')
  flash(strdate+'に追加します', 'success')
  form = JobForm()
  config = Shiftconfig.query.first()
  config.init()
  numlist = [i for i in range(1,11)]
  form.priority.choices = numlist
  form.weight.choices = numlist
  form.employee_priority.choices = numlist
  form.parttime_priority.choices = numlist
  form.helper_priority.choices = numlist

  if request.method == 'POST':
    flash('仕事を追加しました', 'success')
    job = Dayjob(jobname=form.jobname.data, one_date=one_date, starttime=form.starttime.data, endtime=form.endtime.data, priority=form.priority.data , required_number=form.required_number.data, weight=form.weight.data, employee_priority=form.employee_priority.data, parttime_priority=form.parttime_priority.data,helper_priority=form.helper_priority.data,be_indispensable=form.be_indispensable.data)
    db.session.add(job)
    db.session.commit()
    return redirect(url_for("dayjob"))

  flash('仕事を追加します', 'success')
  return render_template('dayjob/new.html',form=form)

@app.route('/dayjob/<int:id>/detail', methods=['GET', 'POST'])
@login_required
@date_chosen
def detail_dayjob(id):
  job = Dayjob.query.get_or_404(id)
  
  return render_template('dayjob/detail.html',job=job)

@app.route('/dayjob/<int:id>/edit', methods=['GET', 'POST'])
@login_required
@date_chosen
def edit_dayjob(id):
  job = Job.query.get_or_404(id)
  form = JobForm()
  config = Shiftconfig.query.first()
  config.init()
  numlist = [i for i in range(1,11)]
  form.priority.choices = numlist
  form.weight.choices = numlist
  form.employee_priority.choices = numlist
  form.parttime_priority.choices = numlist
  form.helper_priority.choices = numlist
  if request.method == "POST":
    flash('編集しました', 'success')
    job.jobname = form.jobname.data
    job.starttime=form.starttime.data
    job.endtime=form.endtime.data
    job.priority = form.priority.data
    job.required_number = form.required_number.data
    job.weight=form.weight.data
    job.employee_priority=form.employee_priority.data
    job.parttime_priority=form.parttime_priority.data
    job.helper_priority=form.helper_priority.data
    job.be_indispensable = form.be_indispensable.data
    db.session.commit()
    return redirect(url_for('dayjob'))
 
  form.jobname.data = job.jobname
  form.starttime.data = job.starttime
  form.endtime.data = job.endtime
  form.priority.data = job.priority
  form.required_number.data = job.required_number
  form.weight.data = job.weight
  form.employee_priority.data = job.employee_priority
  form.parttime_priority.data = job.parttime_priority
  form.helper_priority.data = job.helper_priority
  form.be_indispensable.data = job.be_indispensable
  # print(form.weight.data)
  flash('編集します', 'warning')
  return render_template('dayjob/edit.html',form=form)


@app.route('/dayjob/<int:id>/delete', methods=['GET', 'POST'])
@login_required
@date_chosen
def delete_dayjob(id):
  job = Job.query.get_or_404(id)
  if request.method == "POST":
    flash('削除しました', 'success')
    db.session.delete(job)
    db.session.commit()
    return redirect(url_for('job'))
  elif request.method == "GET":
    flash('削除しますか？', 'warning')
    return render_template('dayjob/delete.html',job=job)