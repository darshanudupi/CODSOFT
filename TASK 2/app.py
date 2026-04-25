from flask import Flask, render_template
from flask_mail import Mail, Message

app = Flask(__name__)

# Email config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your_email@gmail.com'
app.config['MAIL_PASSWORD'] = 'your_app_password'
app.config['MAIL_USE_TLS'] = True

mail = Mail(app)

@app.route('/')
def home():
    return render_template("email.html")

@app.route('/send')
def send_email():
    msg = Message(
        subject="Premium Newsletter 🚀",
        sender='your_email@gmail.com',
        recipients=['receiver@gmail.com']
    )

    msg.html = render_template("email.html")

    mail.send(msg)

    return "Email Sent Successfully!"

if __name__ == '__main__':
    app.run(debug=True)