# Import flask dependencies
from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for

# Import password / encryption helper tools
from werkzeug import check_password_hash, generate_password_hash

# Import the database object from the main app module
from app import db ,app

# Import module forms
from app.home.forms import LoginForm

# Import module models (i.e. User)
from app.home.models import User

# Define the blueprint: 'home', set its url prefix: app.url/home
home = Blueprint('home', __name__, url_prefix='/home')

# Set the route and accepted methods


@app.route('/')
def landing_page():
    return render_template("home/landing_page.html")


@home.route('/', methods=['GET', 'POST'])
def signin():

    # If sign in form is submitted
    form = LoginForm(request.form)

    # Verify the sign in form
    if form.validate_on_submit():

        user = User.query.filter_by(email=form.email.data).first()

        if user and check_password_hash(user.password, form.password.data):

            session['user_id'] = user.id

            flash('Welcome %s' % user.name)

            return redirect(url_for('home.home'))

        flash('Wrong email or password', 'error-message')

    return render_template("home/signin.html", form=form)
