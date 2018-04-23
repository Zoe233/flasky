from datetime import datetime

import sys
import os

current_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT_PATH = os.path.join(current_path, '..')
sys.path.append(ROOT_PATH)

import hashlib # hash算法，主要用于加密相关的操作 md5, sha1, sha224, sha256, sha384, sha512.

from werkzeug.security import generate_password_hash,check_password_hash

# 签名（秘钥），加密签名数据
# itsdangerous内部默认使用了HMAC和SHA1来签名，也支持JSON Web签名（JWS)
# 该库采用BSD协议
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from markdown import markdown
import bleach
from flask import current_app, request, url_for
from flask_login import UserMixin, AnonymousUserMixin
from app.exceptions import ValidationError
# from . import db,login_manager
from app import db
class Permission:
    '''
    权限管理常量
    '''
    FOLLOW = 1
    COMMENT = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16

# db = SQLAlchemy(),flask的sqlalchemy数据库操作管理工具
class Role(db.Model):
    '''
    角色表
    '''
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64), unique = True)
    default = db.Column(db.Boolean, default = False, index = True)
    permissions = db.Column(db.Integer)
    users = db.relationship('User', backref = 'role', lazy = 'dynamic')

    def __init__(self, **kwargs):
        super(Role, self).__init__(**kwargs)
        if self.permissions is None:  # 此处很奇怪，不知道为啥，没看到self.permissions值的初始化，应该会报错，但是没有。wierd
            self.permissions = 0

    @staticmethod
    def insert_roles():
        '''
        新增角色管理权限。
        默认管理权限管理为的内容在roles中，如无指定的角色，则默认为'User'权限。

        '''
        roles = {
            'User': [Permission.FOLLOW, Permission.COMMENT, Permission.WRITE],
            'Moderator': [Permission.FOLLOW, Permission.COMMENT,
                          Permission.WRITE, Permission.MODERATE],
            'Administrator':[
                Permission.FOLLOW, Permission.COMMENT,
                Permission.WRITE, Permission.MODERATE,
                Permission.ADMIN]
        }
        default_role = 'User'
        for r in roles:
            role = Role.query.filter_by(name = r).first()
            # 在数据库中未获取到r则执行 role = Role(name = r)
            # Role(name=r)的返回结果是什么？
            # <Role(name= r> 的对象
            if role is None:
                role = Role(name = r)
            # 初始化，将self.permission设置为0
            role.reset_permissions()
            for perm in roles[r]:
                role.add_permission(perm)
                # 添加角色的指定的权限内容,通过self.permissions+= perm,
                # 每个权限都有指定的数值，可以根据求和数来判断权限是哪些
                # 因为数据库中permissions的字段为数值型
            role.default = (role.name == default_role)
            db.session.add(role)
        db.session.commit()

    def add_permission(self, perm):
        '''
        自定义add_permission方法
        '''
        if not self.has_permission(perm):
            self.permissions += perm

    def remove_permission(self, perm):
        '''
        自定义的移除权限方法
        '''
        if self.has_permission(perm):
            self.permissions -= perm

    def reset_permission(self):
        self.permissions = 0

    def has_permission(self, perm):
        '''
        通过验证传入的perm和self.permission是否一致来判断当前操作的角色的权限是否存在，
        如不一致，则说明需要设置；
        如一致，则说明设置成功，或者初始化时已有相应对应权限。
        :return:一致返回True，不一致返回False
        '''
        return self.permissions & perm == perm

    def __repr__(self):
        '''
        类对象返回的自定义格式
        '''
        return '<Role %r>'% self.name






if __name__=='__main__':
    # class T():
    #     def __init__(self):
    #         if self.p is None:
    #             self.p = 0
    # t = T()

#     role = Role(name='User')

