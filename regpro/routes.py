from flask import render_template, url_for, flash, redirect
from regpro import app
from regpro.forms import RegistrationForm, LoginForm, AddClass
from regpro.models import User
import sys
from BackEnd import RegPro 

sys.path.append("..")
UserDataBase = RegPro.readPickle("UserDataBase.p")
ClassDataBase = RegPro.readPickle("ClassDataBase.p")
currUser = None


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    registration_form = RegistrationForm()

    if registration_form.validate_on_submit():
        flash(f'Account created for {registration_form.username.data}', 'success')
        return redirect(url_for('home'))

    return render_template('signup.html', page='Sign-up', form=registration_form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        username = login_form.username.data
        password = login_form.password.data
        users = UserDataBase.getAllUsers()
        for user in users:
            if user.getID() == username and user.getPassword() == password:
                currUser = user
                return redirect(url_for('student'))

    return render_template('login.html', page='Login', form=login_form)


@app.route('/student')
def student():
    user = currUser
    return render_template('student.html', stu = user)


@app.route('/addDrop')
def addDrop():
    add_form = AddClass()
    return render_template('addDrop.html', classDataBase=ClassDataBase, form=add_form)
