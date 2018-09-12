from flask import Flask, request, render_template, redirect
from wtforms import Form, StringField, PasswordField, validators, BooleanField, SubmitField


class LoginForm(Form):
    username = StringField('username', [validators.data_required()])
    password = PasswordField('password', [validators.data_required()])
    remember = BooleanField('记住我')
    submit = SubmitField('登录')


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    myform = LoginForm(request.form)
    if request.method == 'POST':
        if myform.username.data == 'root' and myform.password.data == 'toor':
            print(myform.remember.data)
            return redirect('http://www.baidu.com')
        else:
            massage = 'Login Failed'
            return render_template('form.html', massage=massage, form=myform)

    return render_template('form.html', form=myform)


if __name__ == '__main__':
    app.run()