from app import app, db
from flask import Flask, request, render_template, redirect
import models

@app.route('/')
def index():
    messages = models.Message.query.order_by(models.Message.id.desc()).all()
    return render_template("index.html", messages=messages)

@app.route('/add_message', methods=['POST'])
def add_message():
    txt = request.form.get('message')
    if not txt:
        abort(500)
    db.session.add(models.Message(txt))
    db.session.commit()
    return redirect('/')

@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()