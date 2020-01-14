from flask import Flask, redirect, request, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    render_template("temp.html", title="Title Value", content="Testing")


if __name__ == "__main__":
    app.run()
