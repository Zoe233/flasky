import os
from dotenv import load_dotenv
# 是一个零依赖的模块，可以从.env文件中读取环境变量到process.env
# 安装：pip install -U python-dotenv

# 使用dotenv模块管理读取.env文件中的环境变量
dotenv_path = os.path.join(os.path.dirname(__file__),'.env')
# 目前在git的源代码中没有看到.env文件，不知道是怎么配置的。目前没有出现，后续使用
# print(dotenv_path) # /Users/zoe/PycharmProjects/flasky/.env
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

# 使用coverage工具统计python单元测试覆盖率
COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True,include='app/*')
    COV.start()

import sys
import click
from flask_migrate import Migrate,Upgrade
from app import create_app,db
from app.models import User,Follow,Role,Permission,Post,Comment

