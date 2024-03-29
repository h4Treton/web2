from flask import Flask, request, redirect, render_template, send_from_directory, url_for
import os
from werkzeug.utils import secure_filename

BASE_DIR = os.getcwd()

app = Flask(__name__, static_folder=os.path.join(BASE_DIR, 'static'),
            template_folder = os.path.join(BASE_DIR, 'templates'))

app.config['SECRET_KEY'] = 'yuhasdfbb[PSDGOHpdofhgpoahghodfgh]'

users = ['user1', 'user2', 'user3', 'user4']

@app.route('/')
def index():
    res = ''
    res += '<h4> USERS </h4>'
    for user in users:
        res += f"<p> пользователь {user} </p>"
    return(res)

@app.route('/users/')
def users2():
    return render_template('1.html', users = users, head = '', color = 'red')

@app.route('/tst/')
def tst2():
    return render_template('2.html', users = users, head = '', color = 'red')

if __name__ == '__main__':
    app.run(debug=True)