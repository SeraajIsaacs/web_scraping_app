from flask import Blueprint, render_template, redirect, url_for, session, flash

main = Blueprint('main', __name__)

# Welcome route (shown before login or registration)
@main.route('/welcome')
def welcome():
    return render_template('welcome.html')  # The welcome page template

# Home route (after login)
@main.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('main.login'))
    return render_template('home/index.html')  # Page content after login

# Login route
@main.route('/auth/login')
def login():
    return render_template('auth/login.html')  # Login page template

# Logout route
@main.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_name', None)
    flash("You have been logged out.", 'success')
    return redirect(url_for('main.login'))
