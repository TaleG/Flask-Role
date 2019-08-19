#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from flask import current_app, jsonify
from flask_restful import Resource
from roles import db
from roles.models import SUP_Permission_Role_Models
from roles.utils import RET

class Role_Permission_View(Resource):
    """Role Link Permission"""
    def get(self, id):
        """
        查询角色所对应的权限
        :return:
        """
        try:
            Permission_Role = SUP_Permission_Role_Models.query.filter_by(roleId=id).first()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.NODATA, codemsg="No Data.")

        try:
            Permission_Role_Info = Permission_Role.to_json()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Data Error.")

        return jsonify(code=RET.OK, codemsg="Succeed.", data=Permission_Role_Info)