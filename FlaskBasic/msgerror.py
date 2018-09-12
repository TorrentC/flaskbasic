from flask import Flask, render_template, flash, request
from flask import abort

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def index():
    flash('Hello everyone')
    return render_template('index.html')


@app.route('/login/', methods=['POST'])
def login():
    username = request.form.get('user')
    pwd = request.form.get('pwd')
    if not username:
        flash('please input username')
        return render_template('index.html')
    if not pwd:
        flash('please input password')
        return render_template('index.html')

    if username == 'root' and pwd == '123456':
        flash('login success')
    else:
        flash('username or password wrong')

    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.route('/user/<int:user_id>')
def user(user_id):
    print(user_id, type(user_id))
    if user_id > 200:
        abort(404)
    return render_template('user.html', id=user_id)


if __name__ == '__main__':
    app.run()