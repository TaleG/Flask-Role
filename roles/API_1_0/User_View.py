#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from flask_restful import Resource
from flask import request, jsonify, current_app
from sqlalchemy.exc import IntegrityError
from roles.utils import RET
from roles.models import Support_User_Models
from roles import db

class Users_List_Views(Resource):
    """用户"""
    def get(self):
        """
        查找所有数据
        :return:
        """
        try:
            User_Data = Support_User_Models.query.all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error.")

        User_List = []
        for User_Info in User_Data:
            User_List.append(User_Info.to_json())

        return jsonify(code=RET.OK, codemsg="Succeed.", data=User_List)

    def post(self):
        """
        添加用户
        :return:
        """
        req_data = request.get_json()
        # 获取用户名和密码，因为要判断是否为空
        password = req_data.get("password")
        username = req_data.get("username")

        # 获取访问IP
        ip = request.remote_addr

        # 判断是否为空
        if not all([username, password]):
            return jsonify(code=RET.NODATA, codemsg='No Data.')

        try:
            # 将数据组到表中
            user = Support_User_Models(
                username=username,
                phone=req_data.get("phone"),
                email=req_data.get("email"),
                mark=req_data.get("mark"),
                lastLogin=req_data.get("lastLogin"),
                loginIp=ip,
                imageUrl=req_data.get("imageUrl"),
            )
            # 使用了property内置方法，只需把password附值传给后台进行hash算法存储即可。
            user.password_bash = password
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Data Error.")

        try:
            # 添加组好的数据到数据库
            db.session.add(user)
            # 提交数据
            db.session.commit()
        except IntegrityError as e:
            # 如果有异常，进行回滚
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DATAEXIST, codemsg='Data Exist.')
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg='Data Error')

        return jsonify(code=RET.OK, codemsg="Succeed.")




