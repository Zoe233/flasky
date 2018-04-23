from flask import Blueprint
'''
项目模块划分阶段，使用Blueprint('蓝本'）。
Blueprint通过把实现不同功能的module分开，从而把一个大的application分隔成各自实现不同功能的module.
在一个Blueprint中可以调用另一个blueprint的view function,但要加相应的blueprint名。
其他好处：让程序更加松耦合，更加灵活，增加复用性，提高查错效率，降低出错概率。
在具体项目开发过程中国，不同蓝本分别对应不同的功能模块。
例如：auth授权模块 和 项目主模块。
'''

main = Blueprint('main',__name__)
from . import views,errors
from ..models import Permission

@main.app_context_processor
def inject_permissions():
    return dict(Permission=Permission)

