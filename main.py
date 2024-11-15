from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello from Flask!</h1>'

@app.route('/prova')
def prova():
    return '<h1>Pagina di prova</h1>'

app.run(host='localhost', port = 3000, debug=True)