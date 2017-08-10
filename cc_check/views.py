from flask import render_template, redirect, url_for, session

from cc_check import app
from cc_check.forms import CCCForm
from cc_check.core import validate_cc_number


@app.route('/', methods=['GET', 'POST'])
def main():
    checks = None
    form = CCCForm()
    if form.validate_on_submit():
        f = form.numbers.data
        N = int(f.readline())
        checks = []
        for _ in range(N):
            number = f.readline().decode('utf-8')
            checks.append((number, validate_cc_number(number)))
    return render_template('index.html', form=form, checks=checks)
