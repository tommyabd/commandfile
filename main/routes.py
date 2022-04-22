from flask import redirect, render_template, request
from main import app
from main.models import Veri
from flask import request
from main import db

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sql/<deger>')
def sql(deger):
    if request.method == "POST":
        content_to_create=Veri(deger=deger)
        db.session.add(content_to_create)
        db.session.commit()
    return redirect(sql)

