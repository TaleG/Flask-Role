#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from flask_restful import Resource
from flask import current_app, jsonify
from roles.models import SUP_User_Role_Models
from roles.utils import RET

class Sup_User_Role_Views(Resource):
    """查找数据"""
    def get(self, id):
        """

        :param id: ID是匹配的用户UID
        :return:
        """
        try:
            # 查询用户所属权限信息
            User_Role_Data = SUP_User_Role_Models.query.filter_by(UserId=id).first()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.NODATA, codemsg="Database Error.")

        try:
            # 按ID查到的数据进行返回
            user_List = User_Role_Data.to_json()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="No Data.")
        return jsonify(code=RET.OK, codemsg="Succeed.", data=user_List)
