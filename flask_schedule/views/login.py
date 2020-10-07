from flask import render_template, url_for, flash, redirect, request, session
from flask_schedule import app


@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None
  if request.method == 'POST':
    if request.form['username'] != app.config['USERNAME']:
      flash('ユーザ名が異なります',"danger")
    elif request.form['password'] != app.config['PASSWORD']:
      flash('パスワードが異なります',"danger")
    else:
      session['logged_in'] = True
      flash('ログインしました',"success")
      return redirect(url_for('index'))
  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('logged_in', None)
  flash('ログアウトしました',"success")
  return redirect(url_for('index'))
