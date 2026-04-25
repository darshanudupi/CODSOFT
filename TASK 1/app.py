from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = "secret123"

# Temporary database (for demo)
users = {}

# ---------------- HOME ----------------
@app.route('/')
def index():
    return render_template('index.html', error=None)


# ---------------- SIGN UP ----------------
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        # Save user
        users[email] = {
            "name": name,
            "password": password
        }

        # Generate OTP
        otp = random.randint(1000, 9999)
        session['otp'] = str(otp)
        session['temp_user'] = email

        print("OTP (for demo):", otp)

        return redirect(url_for('verify'))

    return render_template('signup.html')


# ---------------- OTP VERIFY ----------------
@app.route('/verify', methods=['GET', 'POST'])
def verify():
    if request.method == 'POST':
        user_otp = request.form.get('otp')

        if user_otp == session.get('otp'):
            email = session.get('temp_user')
            session['name'] = users[email]['name']
            return redirect(url_for('success'))
        else:
            return "❌ Invalid OTP"

    return render_template('verify.html')


# ---------------- SIGN IN ----------------
@app.route('/signin', methods=['GET', 'POST'])
def signin():
    error = None

    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email not in users:
            error = "🚫 Account doesn't exist! Please Sign Up."
        elif users[email]['password'] != password:
            error = "❌ Incorrect Password!"
        else:
            session['name'] = users[email]['name']
            return redirect(url_for('success'))

    return render_template('signin.html', error=error)


# ---------------- SUCCESS ----------------
@app.route('/success')
def success():
    return render_template('success.html', name=session.get('name'))


# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)