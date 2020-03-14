from flask import Flask, render_template, request, flash, redirect, url_for, escape, session
import data_manager

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
@app.route('/index.html')
def route():
    if 'username' in session:
        username_info = f"Signed in as {session['username']}"
        return render_template('index.html', username_info = username_info)
    else:
        return render_template("index.html" )

@app.route('/registration', methods=['POST', 'GET'])
def registration():
    registration_data = {}
    if request.method == 'POST':
        if request.form['psw'] != request.form['psw-repeat']:
            flash ('Repeated password must be the same, please try again')
            return render_template("registration.html")
        registration_data['user'] = request.form['user']
        registration_data['email'] = request.form['email']
        registration_data['password'] = request.form['psw']
        registration_data['psw-repeat'] = request.form['psw-repeat']
        register_conf = data_manager.check_user(registration_data)
        if not register_conf:
            flash('User with submitted data already exist.')
            return render_template("registration.html")
        data_manager.add_user(registration_data)
        register_conf = 'Registration successful. Please sign in to continue.'
        return redirect(url_for('login', register_conf=register_conf))
    if 'username' in session:
        username_info = f"Signed in as {session['username']}"
        return render_template('registration.html', username_info=username_info )
    else:
        return render_template("registration.html" )

@app.route('/login', methods=['POST', 'GET'])
def login():

    login_data = {}
    if request.method == 'POST':
        login_data['user'] = request.form['email']
        login_data['email'] = request.form['email']
        login_data['password'] = request.form['psw']

        if not data_manager.check_user(login_data):
            if data_manager.check_login_password(login_data):
                session['username'] = request.form['email']
                return redirect((url_for('route')))
            register_conf = "Wrong email/username or password"
            return render_template("login.html", register_conf=register_conf)
        register_conf = "Wrong email/username or password"
        return render_template("login.html", register_conf=register_conf)

    if 'username' in session:
        username_info = f"Signed in as {session['username']}"
        return render_template('login.html', username_info=username_info)
    else:
        register_conf = request.args['register_conf']
        return render_template("login.html", register_conf=register_conf )

@app.route('/logout')
def logout():
    [session.pop(key) for key in list(session.keys())]
    render_template('index.html')


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )