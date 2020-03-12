from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
@app.route('/index.html')
def route():
    return render_template("index.html" )

@app.route('/registration')
def register():
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