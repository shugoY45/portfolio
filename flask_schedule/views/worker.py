from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import WorkerForm 
from setting import hourlist,minuteslist
from flask_schedule.models import Worker

@app.route('/worker', methods=['GET', 'POST'])
def worker():
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  workers = Worker.query.all()
  form = WorkerForm()
  hour = hourlist
  minutes = minuteslist
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  if request.method == "GET":
    return render_template('worker/worker.html',form=form,workers=workers)
  if request.method == 'POST':
    if form.validate_on_submit():
      flash('従業員を追加しました', 'success')
      worker = Worker(workername=form.workername.data, starttime=form.starttime_hour.data+':'+form.starttime_minutes.data, endtime=form.endtime_hour.data+':'+form.endtime_minutes.data, workerweight='0')
      db.session.add(worker)
      db.session.commit()
      workers = Worker.query.all()
      return render_template('worker/worker.html',form=form,workers=workers)


@app.route('/worker/<int:id>/edit', methods=['GET', 'POST'])
def edit_worker(id):
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  worker = Worker.query.get_or_404(id)
  form = WorkerForm()
  hour = hourlist
  minutes = minuteslist
  form.starttime_hour.choices = hourlist
  form.starttime_minutes.choices = minuteslist
  form.endtime_hour.choices = hourlist
  form.endtime_minutes.choices = minuteslist
  if form.validate_on_submit():
    flash('編集しました', 'success')
    worker.workername = form.workername.data
    worker.starttime=form.starttime_hour.data+':'+form.starttime_minutes.data
    worker.endtime=form.endtime_hour.data+':'+form.endtime_minutes.data
    db.session.commit()
    return redirect(url_for('worker'))
  elif request.method == "GET":
    form.workername.data = worker.workername
    form.starttime_hour.data = worker.starttime.split(':')[0]
    form.starttime_minutes.data = worker.starttime.split(':')[1]
    form.endtime_hour.data = worker.endtime.split(':')[0]
    form.endtime_minutes.data = worker.endtime.split(':')[1]
    flash('編集します', 'warning')
    return render_template('worker/edit.html',form=form,worker=worker)


@app.route('/worker/<int:id>/delete', methods=['GET', 'POST'])
def delete_worker(id):
  if not session.get('logged_in'):
    return redirect(url_for('login'))
  worker = Worker.query.get_or_404(id)
  if request.method == "POST":
    flash('削除しました', 'success')
    db.session.delete(worker)
    db.session.commit()
    return redirect(url_for('worker'))
  elif request.method == "GET":
    flash('削除しますか？', 'warning')
    return render_template('worker/delete.html',worker=worker)
