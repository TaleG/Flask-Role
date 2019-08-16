#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Blueprint
from flask_restful import Api
from . import Begins, User_View, Role_View, Role_User_View

# 创建蓝图对象
api_bp = Blueprint("api_1_0", __name__)
api = Api(api_bp)

# 测试
api.add_resource(Begins.Begin, '/begin', endpoint='begin')

# 用户
api.add_resource(User_View.Users_List_Views, '/userlist', endpoint='userlist')

# 权限
api.add_resource(Role_View.Role_View_List, '/rolelist', endpoint='rolelist')

# 用户&权限
api.add_resource(Role_User_View.Sup_User_Role_Views, '/userrole', '/userrole/<int:id>', endpoint='userrole')
