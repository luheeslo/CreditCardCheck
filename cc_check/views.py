from flask import render_template

from cc_check import app


@app.route('/')
def hello():
    return render_template('index.html')
