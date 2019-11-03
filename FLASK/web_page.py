from flask import Flask, request, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return 'Index Page'
@app.route('/hello')
def hello():
    return 'Hello, World'
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        imie = request.form['imie']
        komentarz = request.form['komentarz']
        return str((imie, komentarz))
    else:
        return render_template('login_page1.html')
app.run()