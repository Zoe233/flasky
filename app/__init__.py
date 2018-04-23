from flask import Flask
# 是Twitter开发的一个开源框架，
# 它提供的用户界面组件可用于创建整洁且具有吸引力的网页，
# 而且这些网页还能兼容所有现代 Web 浏览器。
# 安装：pip install flask-bootstrap
from flask_bootstrap import Bootstrap

# 很多Web应用需要在诸如用户注册、密码找回等过程中，进行用户身份的有效性认证。采用电子邮箱进行确认是一种常用的方式
# Python标准库smtplib可以实现发送电子邮件的功能，
# Flask框架的Flask-mail包装了smtplib库，扩展了对电子邮件发送的支持。
# 安装：pip install flask-mail
from flask_mail import Mail

# Flask-Moment又是一个flask的扩展模块，用来处理时间日期等信息。
# 用这个模块主要是考虑到两点，
# 第一是为了让不同时区的用户看到的都是各自时区的实际时间，而不是服务器所在地的时间。
# 第二是对于一些时间间隔的处理，如果要手动处理很麻烦，如果有模块就很好了。
# 安装：pip install flask-moment
from flask_moment import Moment

# 对数据库进行基本操作
# 安装：pip install flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

# 将我们写的纯文本的博客文章，使用Flask-pagedown模块，
# 将文本转换成html富文本数据，并在浏览器上显示，
# 类似于博客文章的预览功能。
# PageDown是用JavaScript实现的由文本到Html的转换程序，
# 而Flask-pagedown是对PageDown的一个封装，把其集成到了Flask-WTF表单中。
# 安装：pip install flask_pagedown
from flask_pagedown import PageDown
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


