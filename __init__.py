from flask import Flask
# app = Flask(__name__)
# @app.route("/")
# def hello():
#     return "Hello, I really did change this from my computer!"

import views

if __name__ == "__main__":
    views.app.run()
