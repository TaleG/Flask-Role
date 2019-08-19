#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from roles import db

class Support_Role_Models(db.Model):
    """Role List"""
    __tablename__ = "support_role"

    id = db.Column(db.Integer, primary_key=True)
    roleName = db.Column(db.String(32), unique=True, nullable=False)
    roleDesc = db.Column(db.String(128))
    roleList1 = db.relationship("SUP_Permission_Role_Models",
                               backref='support_role', lazy='dynamic')
    roleList2 = db.relationship("SUP_User_Role_Models",
                               backref='support_role', lazy='dynamic')

    def to_json(self):
        json_data = {
            "id": self.id,
            "roleName": self.roleName,
            "roleDesc": self.roleDesc,
        }
        return json_data