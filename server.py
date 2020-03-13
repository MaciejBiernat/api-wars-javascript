from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
@app.route('/index.html')
def route():
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



        print(registration_data)

        return render_template("registration.html")




    return render_template("registration.html" )

@app.route('/login')
def login():
    return render_template("login.html" )

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )