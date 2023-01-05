from flask import Flask, Blueprint

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "Login"

def signup():
    return 