#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from flask import current_app, request, jsonify
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from roles import db
from roles.utils import RET
from roles.models import Support_Role_Models

class Role_View_List(Resource):
    """权限"""
    def get(self):
        """
        权限列表
        :return:
        """
        try:
            # 获取所有Role数据库数据
            Role_Data = Support_Role_Models.query.all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error.")

        # 做一个容器，把数据存到列表中
        Role_List = []
        # 循环数据库数据，逐步导入列表中
        for Role_Info in Role_Data:
            # 使用append把遍例的数据导入Role_List列表中
            Role_List.append(Role_Info.to_json())

        return jsonify(code=RET.OK, codemsg='Succeed.', data=Role_List)

    def post(self):
        """
        添加权限
        :return:
        """
        # 使用request获取前端返回的数据。类型：{"roleName": "rolename", "roleDesc": "roledesc"}
        req_data = request.get_json()

        # 从前端返回的数据表中get到roleName和roleDesc数据做为对象。
        roleName = req_data.get("roleName")
        roleDesc = req_data.get("roleDesc")

        # 判断前端返回的数据是否为家
        if not all([roleName, roleDesc]):
            return jsonify(code=RET.NODATA, codemsg="No Data.")

        try:
            # 组数据库相应数据
            role = Support_Role_Models(
                roleName=roleName,
                roleDesc=roleDesc
            )
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DATAERR, codemsg='Data Error.')

        try:
            # 添加数据到数据库
            db.session.add(role)
            # 提交数据到数据库
            db.session.commit()
        except IntegrityError as e:
            # 有数据异常做数据回滚
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DATAEXIST, codemsg="Data Exist.")
        except Exception as e:
            # 有数据异常做数据回滚
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error.")

        return jsonify(code=RET.OK, codemsg="Succeed.")


