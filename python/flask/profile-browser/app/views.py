from app import app, lm, oid
from flask import Flask, request, render_template, redirect, g, session, url_for
from database import db_session
from flask.ext.login import login_user, logout_user, current_user, login_required
from forms import LoginForm
from models import User, ROLE_USER, ROLE_ADMIN

@app.route('/')
@app.route('/index')
@login_required
def index():
    user = g.user
    return render_template('index.html', user=user)


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/login', methods = ['GET', 'POST'])
@oid.loginhandler
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        session['remember_me'] = form.remember_me.data
        return oid.try_login('https://www.google.com/accounts/o8/id', ask_for = ['nickname', 'email'])
        
    return render_template('login.html', 
        title = 'Sign In',
        form = form)

@oid.after_login
def after_login(resp):
    print "in after_login"
    if resp.email is None or resp.email == "":
        flash('Invalid login. Please try again.')
        return redirect(url_for('login'))
    user = User.query.filter_by(email = resp.email).first()
    if user is None:
        nickname = resp.nickname
        if nickname is None or nickname == "":
            nickname = resp.email.split('@')[0]
        user = User(nickname = nickname, email = resp.email, role = ROLE_USER)
        db_session.add(user)
        db_session.commit()
    remember_me = False
    if 'remember_me' in session:
        remember_me = session['remember_me']
        session.pop('remember_me', None)
    login_user(user, remember = remember_me)
    return redirect(url_for('index'))

@app.before_request
def before_request():
    g.user = current_user

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
