from flask import Flask, render_template, request, redirect
from psycopg2 import connect, OperationalError

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        amount = request.form.get('amount')
        add_product(name, price, amount)
        return redirect('/')
    else:
        r = get_products()
        return render_template('shop.html', data=r)

def get_products():
    username = "postgres"
    passwd = "coderslab"
    hostname = "127.0.0.1"  # lub "localhost"
    db_name = "shop"
    try:
        # tworzymy nowe połączenie
        cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute("select name, price, amount from product")
        l = cursor.fetchall()
        cnx.close()
        return l
    except OperationalError as e:
        print(e)


def add_product(name, price, amount):
    username = "postgres"
    passwd = "coderslab"
    hostname = "127.0.0.1"  # lub "localhost"
    db_name = "shop"
    try:
        # tworzymy nowe połączenie
        cnx = connect(user=username, password=passwd, host=hostname, database=db_name)
        cnx.autocommit = True
        cursor = cnx.cursor()
        cursor.execute("insert into Product(name, price, amount) values (%s, %s, %s)", [name, price, amount])
        cnx.close()
    except OperationalError as e:
        print(e)



if __name__ == '__main__':
    app.run(debug=True)