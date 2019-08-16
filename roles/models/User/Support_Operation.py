#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from roles import db

class Support_Operation_Models(db.Model):
    """Operation List"""
    __tablename__ = "support_operation"

    id = db.Column(db.Integer, primary_key=True)
    odesc = db.Column(db.String(128))
    name = db.Column(db.String(32))
    operation = db.Column(db.String(128))
    Operation_list = db.relationship("SUP_Permission_Operation_Models",
                                     backref='support_operation', lazy='dynamic')

    def to_json(self):
        json_data = {
            "id": self.id,
            "odesc": self.odesc,
            "name": self.name,
            "operation": self.operation
        }
        return json_data