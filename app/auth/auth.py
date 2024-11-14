from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import generate_password_hash
from app.models import db, User  # Adjusted import path

auth = Blueprint('auth', __name__)

# Add a route for registration
@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match.", 'danger')
            return redirect(url_for('auth.register'))

        # Check password length
        if len(password) < 8:
            flash("Password must be at least 8 characters long.", 'danger')
            return redirect(url_for('auth.register'))

        # Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered.", 'danger')
            print(f"User {email} already exists.")  # Debug print
            return redirect(url_for('auth.register'))

        # Hash the password before saving it to the database
        hashed_password = generate_password_hash(password)
        new_user = User(name=name, surname=surname, email=email, password_hash=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Registration successful!", 'success')

            # Optional: Add a check to verify if the user is added to the database
            created_user = User.query.filter_by(email=email).first()
            if created_user:
                print(f"User {created_user.name} {created_user.surname} added to the database.")
            else:
                print("Failed to add user to the database.")

        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {str(e)}", 'danger')
            print(f"Error: {e}")
            return redirect(url_for('auth.register'))

        return redirect(url_for('auth.login'))

    return render_template('auth/register.html')


# Add a route for login
# Login route with session handling
# Login route with session handling
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            flash("Login successful!", 'success')
            
            # Store user ID in session to track if they are logged in
            session['user_id'] = user.id
            
            # Redirect to the home page after login
            return redirect(url_for('home.index'))  # Redirect to home.index (home page)
        else:
            flash("Invalid credentials. Please try again.", 'danger')
            return redirect(url_for('auth.login'))

    return render_template('auth/login.html')  # Render login page


# Add a route for forgot password
@auth.route('/forgot_password', methods=['GET', 'POST'])
def forgot_password():
    if request.method == 'POST':
        email = request.form['email']
        user = User.query.filter_by(email=email).first()

        if user:
            # Here you would add logic to send a reset password email
            flash("If the email is registered, you will receive instructions on how to reset your password.", 'info')
        else:
            flash("Email not found in our system.", 'danger')
        
        return redirect(url_for('auth.login'))  # Redirect to login after processing the request

    return render_template('auth/forgot_password.html')

# Optional: Add a route to handle password reset (you can adjust this as per your needs)
@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    # Logic to verify the token and allow the user to reset their password.
    # For now, we assume the token verification is handled here.
    return render_template('auth/reset_password.html')

# Logout route to clear session
@auth.route('/logout')
def logout():
    session.pop('user_id', None)  # Remove user_id from session
    flash("You have been logged out.", 'info')
    return redirect(url_for('auth.login'))  # Redirect to the login page
