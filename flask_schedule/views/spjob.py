from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import SpJobForm
# from setting import hourlist,minuteslist, priorty_list
from flask_schedule.models import SpecialJob,Worker,Shiftconfig
from flask_schedule.views.login import login_required



@app.route('/spjob', methods=['GET', 'POST'])
@login_required
def spjob():
  spjobs = SpecialJob.query.all()
  form = SpJobForm()
  worker_list = []
  workers = Worker.query.all()
  config = Shiftconfig.query.first()
  config.init()
  for worker in workers:
    worker_list.append(worker.workername)
  form.workername.choices = worker_list
  form.priority.choices = config.priorty_list
  if request.method == "GET":
    return render_template('spjob/spjob.html',form=form,spjobs=spjobs)
  if request.method == 'POST':
    if form.validate_on_submit():
      flash('固定シフトを追加しました', 'success')
      spjob = SpecialJob(workername=form.workername.data,jobname=form.jobname.data, starttime=form.starttime.data, endtime=form.endtime.data, priority=form.priority.data,)
      db.session.add(spjob)
      db.session.commit()
      spjobs = SpecialJob.query.all()
      return render_template('spjob/spjob.html',form=form,spjobs=spjobs)
    else:
      print(1)

@app.route('/spjob/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_spjob(id):
  spjob = SpecialJob.query.get_or_404(id)
  form = SpJobForm()
  worker_list = []
  workers = Worker.query.all()
  config = Shiftconfig.query.first()
  config.init()
  for worker in workers:
    worker_list.append(worker.workername)
  form.workername.choices = worker_list
  form.priority.choices = config.priorty_list
  form.submit.label = '追加'
  if form.validate_on_submit():
    flash('編集しました', 'success')
    spjob.workername = form.workername.data
    spjob.jobname = form.jobname.data
    spjob.starttime=form.starttime.data
    spjob.endtime=form.endtime.data
    spjob.priority = form.priority.data
    db.session.commit()
    return redirect(url_for('spjob'))
  elif request.method == "GET":
    form.workername.data = spjob.workername
    form.jobname.data = spjob.jobname
    form.starttime.data = spjob.starttime
    form.endtime.data = spjob.endtime
    form.priority.data = spjob.priority
    flash('編集します', 'warning')
    return render_template('spjob/edit.html',form=form,spjob=spjob)


@app.route('/spjob/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_spjob(id):
  spjob = SpecialJob.query.get_or_404(id)
  if request.method == "POST":
    flash('削除しました', 'success')
    db.session.delete(spjob)
    db.session.commit()
    return redirect(url_for('spjob'))
  elif request.method == "GET":
    flash('削除しますか？', 'warning')
    return render_template('spjob/delete.html',spjob=spjob)