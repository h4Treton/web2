from flask import Flask
from flask import send_file

def index_r():
    with open('1.html', 'r', encoding='utf-8') as f:
        res = f.read()
    return res.encode('utf-8')

def cat2_r():
    with open('2.html', 'r', encoding='utf-8') as f:
        res = f.read()
    return res.encode('utf-8')

def send_file2(file_name):
    print(file_name)
    try:
        return(send_file(file_name + '.jpg', mimetype='image/gif', as_attachment = False))
    except FileNotFoundError:
        return('Error')

app = Flask(__name__)


@app.route('/')
def index():
    return(index_r())

@app.route('/cat2/')
def cat2():
    return(cat2_r())

@app.route('/<name>.jpg')
def pic(name):
    return(send_file2(name))

@app.route('/cats/')
def cats():
    return('Hello from cats')

@app.route('/cat/<int:id>')
def cat_num(id):
    return(f'Hello from cat with number {id}')

@app.route('/cat/<string:id>')
def cat_err(id):
    return(f'BAD ID')


app.run(debug=True)
#app.run()