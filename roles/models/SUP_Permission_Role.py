#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from roles import db
from .User import Support_Permission_Models, Support_Role_Models

class SUP_Permission_Role_Models(db.Model):
    """ Role And Permission Link"""

    __tablename__ = 'permission_role'
    id = db.Column(db.Integer, primary_key=True)
    permissionId = db.Column(db.ForeignKey(Support_Permission_Models.id))
    roleId = db.Column(db.ForeignKey(Support_Role_Models.id))

    def to_json(self):
        json_data = {
            "id": self.id,
            "roleId": self.support_role.id,
            "permissionId": self.support_permission.id,
            "roleName": self.support_role.roleName,
            "roleDesc": self.support_role.roleDesc,
            "permissionName": self.support_permission.name,
            "permissionPdesc": self.support_permission.pdesc
        }
        return json_data
