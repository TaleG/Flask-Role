#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask import Blueprint
from flask_restful import Api
from . import Begins, User, Role, Role_User, Permission, Operation, Role_Permission

# 创建蓝图对象
api_bp = Blueprint("api_1_0", __name__)
api = Api(api_bp)

# 测试
api.add_resource(Begins.Begin, '/begin', endpoint='begin')

# 用户
api.add_resource(User.Users_List_Views, '/userlist', endpoint='userlist')

# 角色
api.add_resource(Role.Role_View_List, '/rolelist', endpoint='rolelist')

# 用户&角色
api.add_resource(Role_User.Sup_User_Role_Views, '/userrole', '/userrole/<int:id>', endpoint='userrole')

# 权限
api.add_resource(Permission.Permission_View, '/permission', endpoint='permission')

# 操作
api.add_resource(Operation.Operation_View, '/operation', endpoint='operation')

#  权限&操作
api.add_resource(Role_Permission.Role_Permission_View, '/rolepermission', '/rolepermission/<int:id>', endpoint='rolepermission')
