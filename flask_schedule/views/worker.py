from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app, db
from flask_schedule.forms import WorkerForm
from flask_schedule.models import Worker, Shiftconfig
from flask_schedule.views.login import login_required
from flask_schedule.views.views import date_chosen


@app.route('/worker', methods=['GET', 'POST'])
@login_required
def worker():
  date = session['date']
  workers = Worker.query.all()
  return render_template('worker/worker.html',workers=workers,date=date)

@app.route('/worker/new', methods=['GET', 'POST'])
@login_required
def new_worker():
  date = session['date']
  form =WorkerForm()
  if request.method == "POST":
    if form.validate_on_submit():
      flash('追加しました', 'success')
      Sun = request.form.get("Sun")
      Mon = request.form.get("Mon")
      Tue = request.form.get("Tue")
      Wed = request.form.get("Wed")
      Thu = request.form.get("Thu")
      Fri = request.form.get("Fri")
      Sat = request.form.get("Sat")
      worker = Worker()
      worker.workername = form.workername.data
      if Sun:
        worker.Sun = True
      else :
        worker.Sun = False
      worker.Sunstarttime=form.Sunstarttime.data
      worker.Sunendtime=form.Sunendtime.data
      if Mon:
        worker.Mon = True
      else :
        worker.Mon = False
      worker.Monstarttime=form.Monstarttime.data
      worker.Monendtime=form.Monendtime.data

      if Tue:
        worker.Tue = True
      else :
        worker.Tue = False
      worker.Tuestarttime=form.Tuestarttime.data
      worker.Tueendtime=form.Tueendtime.data

      if Wed:
        worker.Wed = True
      else :
        worker.Wed = False
      worker.Wedstarttime=form.Wedstarttime.data
      worker.Wedendtime=form.Wedendtime.data

      if Thu:
        worker.Thu = True
      else :
        worker.Thu = False
      worker.Thustarttime=form.Thustarttime.data
      worker.Thuendtime=form.Thuendtime.data

      if Fri:
        worker.Fri = True
      else :
        worker.Fri = False
      worker.Fristarttime=form.Fristarttime.data
      worker.Friendtime=form.Friendtime.data

      if Sat:
        worker.Sat = True
      else :
        worker.Sat = False
      worker.Satstarttime=form.Satstarttime.data
      worker.Satendtime=form.Satendtime.data
      
      db.session.add(worker)
      db.session.commit()

      return redirect(url_for('worker'))
    else:
      return render_template('worker/new.html',form=form)
  elif request.method == "GET":
    return render_template('worker/new.html',form=form)

@app.route('/worker/<int:id>/detail', methods=['GET', 'POST'])
@login_required
def worker_detail(id):
  worker = Worker.query.get_or_404(id)
  return render_template('worker/detail.html',worker=worker)

@app.route('/worker/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_worker(id):
  worker = Worker.query.get_or_404(id)
  form = WorkerForm()
  if request.method == "POST":
    if form.validate_on_submit():
      flash('編集しました', 'success')
      Sun = request.form.get("Sun")
      Mon = request.form.get("Mon")
      Tue = request.form.get("Tue")
      Wed = request.form.get("Wed")
      Thu = request.form.get("Thu")
      Fri = request.form.get("Fri")
      Sat = request.form.get("Sat")
      worker.workername = form.workername.data
      if Sun:
        worker.Sun = True
      else :
        worker.Sun = False
      worker.Sunstarttime=form.Sunstarttime.data
      worker.Sunendtime=form.Sunendtime.data
      if Mon:
        worker.Mon = True
      else :
        worker.Mon = False
      worker.Monstarttime=form.Monstarttime.data
      worker.Monendtime=form.Monendtime.data
      if Tue:
        worker.Tue = True
      else :
        worker.Tue = False
      worker.Tuestarttime=form.Tuestarttime.data
      worker.Tueendtime=form.Tueendtime.data
      if Wed:
        worker.Wed = True
      else :
        worker.Wed = False
      worker.Wedstarttime=form.Wedstarttime.data
      worker.Wedendtime=form.Wedendtime.data
      if Thu:
        worker.Thu = True
      else :
        worker.Thu = False
      worker.Thustarttime=form.Thustarttime.data
      worker.Thuendtime=form.Thuendtime.data
      if Fri:
        worker.Fri = True
      else :
        worker.Fri = False
      worker.Fristarttime=form.Fristarttime.data
      worker.Friendtime=form.Friendtime.data
      if Sat:
        worker.Sat = True
      else :
        worker.Sat = False
      worker.Satstarttime=form.Satstarttime.data
      worker.Satendtime=form.Satendtime.data
      db.session.commit()
      return redirect(url_for('worker'))
    else:
      raise EnvironmentError("validation error")
  else:
    form.workername.data = worker.workername
    day = Editday()
    day.init()
    if worker.Sun:
      form.Sunstarttime.data = worker.Sunstarttime
      form.Sunendtime.data = worker.Sunendtime
      day.Sunday = "checked"
    if worker.Mon:
      form.Monstarttime.data = worker.Monstarttime
      form.Monendtime.data = worker.Monendtime
      day.Monday = "checked"
    if worker.Tue:
      form.Tuestarttime.data = worker.Tuestarttime
      form.Tueendtime.data = worker.Tueendtime
      day.Tuesday = "checked"
    if worker.Wed:
      form.Wedstarttime.data = worker.Wedstarttime
      form.Wedendtime.data = worker.Wedendtime
      day.Wednesday = "checked"
    if worker.Thu:
      form.Thustarttime.data = worker.Thustarttime
      form.Thuendtime.data = worker.Thuendtime
      day.Thursday = "checked"
    if worker.Fri:
      form.Fristarttime.data = worker.Fristarttime
      form.Friendtime.data = worker.Friendtime
      day.Friday = "checked"
    if worker.Sat:
      form.Satstarttime.data = worker.Satstarttime
      form.Satendtime.data = worker.Satendtime
      day.Saturday = "checked"
    flash('編集します', 'warning')
    return render_template('worker/edit.html',form=form,day=day)

class Editday():
  def init(self):
    self.Sunday= ""
    self.Monday= ""
    self.Tuesday= ""
    self.Wednesday= ""
    self.Thursday= ""
    self.Friday= ""
    self.Saturday= ""


@app.route('/worker/<int:id>/delete', methods=['GET', 'POST'])
@login_required
def delete_worker(id):
  worker = Worker.query.get_or_404(id)
  if request.method == "POST":
    flash('削除しました', 'success')
    db.session.delete(worker)
    db.session.commit()
    return redirect(url_for('worker'))
  elif request.method == "GET":
    flash('削除しますか？', 'warning')
    return render_template('worker/delete.html',worker=worker)




