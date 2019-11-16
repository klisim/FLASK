from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/login')
def hello():
    return 'Hello World'

app.run()


