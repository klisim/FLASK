from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '''<!doctype html>
    <html>
    <head>
    <title>Witamy</title>
    </head>
    <body>
    <h1>Coderslab</h1>
    <p>Strona 1</p>
    </body>
    </html>
    '''
app.run()