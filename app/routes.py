from app import app
from flask import render_template, request, redirect, url_for, flash
from app.forms import LoginForm


users = {
    "ryan_gosling": "gosling555",
    "user1": "mypassword"
}


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
         'author': {'username': 'John'},
         'body': 'Beautiful day in Portland!'
        },
        {
          'author': {'username': 'Susan'},
          'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if username in users and users[username] == password:
            flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        else:
            flash('Неверный логин или пароль!')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


