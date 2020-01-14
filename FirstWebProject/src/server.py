from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/')
def hello():
    return "Hello Indian to the whole World!"

@app.route('/<name>')
def user(name):
    return f"Hello {name}!"

@app.route('/admin')
def admin():
    return redirect(url_for("user", name="Admin!"))

@app.route('/login')
def login():
    return "User Name: <input type='text'><br><br>Password: &nbsp;&nbsp;&nbsp;<input type='password'><br>"




if __name__ == '__main__':
    app.run()