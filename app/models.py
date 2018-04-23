from datetime import datetime
import hashlib # hash算法，主要用于加密相关的操作 md5, sha1, sha224, sha256, sha384, sha512.
from werkzeug.security import generate_password_hash,check_password_hash

# 签名（秘钥），加密签名数据
# itsdangerous内部默认使用了HMAC和SHA1来签名，也支持JSON Web签名（JWS)
# 该库采用BSD协议
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from markdown import markdown
import bleach
from flask import current_app,request,url_for
from flask_login import UserMixin,AnonymousUserMixin
from app.exceptions import ValidationError
from . import db,login_manager

