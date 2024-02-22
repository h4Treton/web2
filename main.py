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


app.run(debug=True)