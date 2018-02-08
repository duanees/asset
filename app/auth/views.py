from flask import render_template, request,redirect, url_for
from app.auth import auth
from app.db import util
from app.auth.forms import LoginForm
import hashlib
# @auth.route('/login', methods=['GET'])
# def login_form():
#     return render_template('auth/login.html')

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = form.name.data
        password = hashlib.md5(form.password.data).hexdigest()
        user = util.get_user(name=name)
        if user and password == user.password_hash:
            return redirect(url_for('main.inventory'))
    # name = request.form.get('username',None)
    # password = request.form.get('password',None)
    return render_template('auth/login.html', form=form)
