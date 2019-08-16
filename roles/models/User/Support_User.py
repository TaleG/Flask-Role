#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from roles import db
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

class Support_User_Models(db.Model):
    """User List"""
    __tablename__ = "support_user"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    password = db.Column(db.String(128))
    phone = db.Column(db.String(11))
    email = db.Column(db.String(32))
    mark = db.Column(db.String(128))
    lastLogin = db.Column(db.String(32))
    loginIp = db.Column(db.String(32))
    imageUrl = db.Column(db.String(128))
    regTime = db.Column(db.String(32))
    locked = db.Column(db.Boolean)
    user_List = db.relationship("SUP_User_Role_Models",
                                backref='support_user', lazy='dynamic')

    def to_json(self):
        json_data = {
            "id": self.id,
            "username": self.username,
            "phone": self.phone,
            "email": self.email,
            "mark": self.mark,
            "lastLogin": self.lastLogin,
            "loginIp": self.loginIp,
            "imageUrl": self.imageUrl,
            "regTime": self.regTime,
            "locked": self.locked
        }
        return json_data

    @property
    def password_bash(self):
        """
        读取信息
        :return:
        """
        raise AttributeError("This property can only be set. not read.")

    @password_bash.setter
    def password_bash(self, value):
        """
        设置属性    user.password = 'XXX'
        :param value: 设置属性时的数据  value就是"XXX"    源始明文密码
        :return:
        """
        self.password = generate_password_hash(value)

    def check_password(self, passwd):
        """
        检验密码的正确证
        :param passwd: 用户登录时填写的原始密码
        :return: 如果正确返回True，否则返回False
        """
        return check_password_hash(self.password, passwd)

    # 为token串设置有效期为：3600 * 24 * 7
    def generate_auth_token(self, expiration=3600 * 24 *7):
        """

        :param expiration:
        :return:
        """
        s = Serializer(current_app.config['SECRET_KEY'], expires_in=expiration)
        token = s.dumps({'id': self.id, 'name': self.username}).decode('ascii')
        return token