一个最简单的flask程序
```
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return "<b>Hello world</b>"


if __name__ == '__main__':
    app.run()
```
## flask基础操作
```
from flask import Flask, request, make_response, abort


app = Flask(__name__)


@app.route('/')
def hello():
    content = "<h1>Welcome here</h><br><a href='/user'>click</a>"
    response = make_response(content)
    response.set_cookie('name', 'Torrent')
    return response


@app.route('/user')
def user():
    name = request.cookies.get('name')
    if name is None:
        abort(404)
    return '<b>Hello %s</b>' % name, 400


if __name__ == '__main__':
    app.run()
```
## 模板的使用

1、使用双括号表示一个变量
{{ name }}
 常用变量过滤器
safe：禁用转义
capitalize：把变量值的首字母转成大写，其余字母转小写
lower：把值转成小写
upper：把值转成大写

2、for循环
{% for comment in comments %}
        {{ comment }}
{% endfor %}
3、判断

{% if name %}
    {{ name }}
{% else %}
    <p>None</p>
{% endif %}

4、定义函数
{% macro li(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}

4、导入模块
{{import 'macro.html' as m}}
使用
{{m.li(name)}}
导入常用部分
{% include 'part.html' %}
5 、模板继承
父模板
{%block title%}Title{%endblock%}
子模板
{%extends 'base.html'%}
{%block title%}
{{super()}}继承父类内容
{%endblock%}
##Bootstrap
```
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
```
继承bootstrap模板
```
{% extends 'bootstrap/base.html' %}
{% block content %}
    <div class="page-header">
        <h1>Hello</h1>
    </div>
{%endblock%}
```
bootstrap常用块名
title styles body navbar content scripts
## 自定义错误页面
```
@app.errorhandler(404)
def page_not_found(e):
    abort(500)
    return render_template('error.html', error=e)

@app.errorhandler(500)
def page_not_found(e):
    return render_template('error.html', error=e)
```
## 链接
url_for('index', name='Torrent', _external=True)
支持参数，和完全url
## 静态链接
    <link rel="shortcut icon" href="{{ url_for('static', filename='favicon.ico') }}" type="image/x-icon">

## flask-moment
```
from flask_moment import Moment
moment = Moment(app)

<p>{{ moment(current_time).format('LLL') }}</p>
    <p>{{ moment(current_time).fromNow(refresh=True) }}</p>

{% block scripts %}
    {{ super() }}
    {{ moment.include_moment() }}
    {{ moment.lang('zh-cn') }}
{% endblock %}
```



