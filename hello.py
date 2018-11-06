from flask import Flask, request, session, abort, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'
bootstrap = Bootstrap(app)
moment = Moment(app)



@app.route('/')
def hello():
    session['name'] = 'Torrent'
    return render_template('child.html', current_time=datetime.utcnow())


@app.route('/user')
def user():
    name = session.get('name')
    comments = range(10)
    if name is None:
        abort(404)
    return render_template('index.html', name=name, comments=comments)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html', error=e)


@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error=e)


if __name__ == '__main__':
    app.run()