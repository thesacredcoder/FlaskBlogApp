from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('notFound.html'), 404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('internalError.html'), 500