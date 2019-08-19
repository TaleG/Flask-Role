#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from flask import current_app, jsonify, request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from roles import db
from roles.models import Support_Operation_Models
from roles.utils import RET

class Operation_View(Resource):
    """操作管理"""
    def get(self):
        """
        查询操作
        :return:
        """
        try:
            Operation_Data = Support_Operation_Models.query.all()
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg='Database Error')

        Operation_List = []

        for Operation_Info in Operation_Data:
            Operation_List.append(Operation_Info.to_json())

        return jsonify(code=RET.OK, codemsg="Succeed.", data=Operation_List)

    def post(self):
        """
        添加操作
        :return:
        """
        req_data = request.get_json()
        odesc = req_data.get("odesc")
        name = req_data.get("name")
        operation = req_data.get("operation")

        if not all([name, operation, odesc]):
            return jsonify(code=RET.NODATA, codemsg="No Data.")

        try:
            operation_data = Support_Operation_Models(
                odesc=odesc,
                name=name,
                operation=operation
            )
        except Exception as e:
            current_app.logger.error(e)
            return jsonify(code=RET.DATAERR, codemsg="Data Error.")

        try:
            db.session.add(operation_data)
            db.session.commit()
        except IntegrityError as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DATAEXIST, codemsg="Data Exist")
        except Exception as e:
            db.session.rollback()
            current_app.logger.error(e)
            return jsonify(code=RET.DBERR, codemsg="Database Error")

        return jsonify(code=RET.OK, codemsg="Succeed.")