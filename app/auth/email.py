from flask_mail import Mail, Message
from flask import current_app as app
import time

mail = Mail()

def send_reset_email(user, token):
    msg = Message("Password Reset Request",
                  sender=app.config["MAIL_USERNAME"],
                  recipients=[user.email])
    msg.body = f"Your reset token is {token}. This token expires in 30 minutes."
    mail.send(msg)
