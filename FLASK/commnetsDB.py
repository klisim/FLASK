from flask import Flask, request, render_template
from psycopg2 import connect, OperationalError
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def comments():
    if request.method == 'POST':
        imie = request.form['imie']
        komentarz = request.form['komentarz']
        add_comment(imie, komentarz)
        return "Komentarz zapisany"
    else:
        return render_template('login_page1.html')
def add_comment(name, comment):
    username = "postgres"
    passwd = "coderslab"
    hostname = "127.0.0.1"  # lub "localhost"
    db_name = "commentsdb"
    try:
        # tworzymy nowe połączenie
        cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
        cnx.autocommit = True
        print("Połączenie udane.")
        cursor = cnx.cursor()
        cursor.execute(f"insert into comments(name, comment, time) values('{name}', '{comment}', 'now');")
        cnx.close()
    except OperationalError as e:
        print(e)
app.run()