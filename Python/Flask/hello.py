from flask import Flask
from flask import, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return 'Yo'

@app.route('/login')
def login():
    username = input("Username ")
    password = input("Password ")

@app.route('/hi')
def index():
    return 'Hi person'

if __name__ == '__main__':
    app.debug = True
    app.run()