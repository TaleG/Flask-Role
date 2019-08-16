#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from roles import db

class Support_Permission_Models(db.Model):
    """Permission List"""
    __tablename__ = "support_permission"

    id = db.Column(db.Integer, primary_key=True)
    pdesc = db.Column(db.String(128))
    name = db.Column(db.String(32))

    Permission_to_list1 = db.relationship("SUP_Permission_Operation_Models",
                                          backref='support_permission', lazy='dynamic')
    Permission_to_list2 = db.relationship("Permission_Role_Models",
                                          backref="support_permission", lazy='dynamic')
    Permission_to_list3 = db.relationship("Permission_Menu",
                                          backref="support_permission", lazy='dynamic')

    def to_json(self):
        json_data = {
            "id": self.id,
            "pdesc": self.pdesc,
            "name": self.name
        }
        return json_data