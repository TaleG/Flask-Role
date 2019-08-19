#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from flask import current_app, jsonify, request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from roles import db
from roles.models import Support_Permission_Models
from roles.utils import RET

class Permission_View(Resource):
    """权限管理"""
    def get(self):
        """
        查询权限
        :return:
        """
        try:
            Permission_Data = Support_Permission_Models.query.all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error.")

        Permission_List = []
        for permission_info in Permission_Data:
            Permission_List.append(permission_info.to_json())

        return jsonify(code=RET.OK, codemsg="Succeed.", data=Permission_List)

    def post(self):
        """
        添加权限
        :return:
        """

        req_data = request.get_json()
        Pdesc = req_data.get("pdesc")
        name = req_data.get("name")

        if not all([Pdesc, name]):
            return jsonify(code=RET.NODATA, codemsg="No Data.")

        try:
            permission = Support_Permission_Models(
                pdesc=Pdesc,
                name=name
            )
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DATAERR, codemsg="Data Error.")

        try:
            db.session.add(permission)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DATAEXIST, codemsg="Data Exist.")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error.")

        return jsonify(code=RET.OK, codemsg="Succeed.")