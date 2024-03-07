from flask import Flask, request
from flask import render_template
import os


from models import db2, Quiz, Question, db_add_new_data

BASE_DIR = os.getcwd()

DB_PATH = os.path.join(BASE_DIR, 'db', 'db_quiz.db')

app = Flask(__name__, template_folder= os.path.join(BASE_DIR, 'templates'))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_PATH}'
app.config['SECRET_KEY'] = 'aseeeeeeeeeeadskjgkcvioem'

db2.init_app(app)

with app.app_context():
    db_add_new_data()

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        quizes = Quiz.query.all()
        return render_template('start.html', quizes)