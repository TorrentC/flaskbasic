# flash消息闪现 自定制404 form表单验证


## flash
```
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
```
```
<div class="alert alert-success"><p class="text-center">{{ get_flashed_messages()[0] }}</p></div>
```
## 404
```
from flask import abort

abort(404)
@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')
```
## form表单
```
from flask import Flask, request, render_template, redirect
from wtforms import Form, StringField, PasswordField, validators, BooleanField, SubmitField


class LoginForm(Form):
    username = StringField('username', [validators.data_required()])
    password = PasswordField('password', [validators.data_required()])
    remember = BooleanField('记住我')
    submit = SubmitField('登录')
```
```
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

```
```
<div align="center" >
        <form action="/" method="post">
            <h1>User Manage</h1>
            {% if massage %}
                {{ massage }}
                <br>
            {% endif %}
        用户：{{ form.username }}

        <br>
        密码：{{ form.password }}
            <br>
        {{ form.remember.label }}
        {{ form.remember }}
        <br>
        {{ form.submit }}
        </form>
    </div>
```
