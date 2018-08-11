from flask import render_template, url_for, flash, redirect, request
from app import micro
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse



@micro.route('/')
@micro.route('/index')
@login_required
def index():
    title = 'Welcome to Flask'
    posts = [
        {
            'author': {'username': 'NotAli'},
            'post': 'What is Flask?'
        },
        {
            'author': {'username': 'MaybeAli'},
            'post': "I don't know what I am doing!"
        }
    ]
    return render_template('/index.html', title=title, posts=posts)

@micro.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    title = 'Login'
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        #flash('Login request for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect(next_page)
    return render_template('login.html', title=title, form=form)

@micro.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))