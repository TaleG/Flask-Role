#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from roles import db
from .User import Support_User_Models, Support_Role_Models

class SUP_User_Role_Models(db.Model):
    """User And Role Link Table"""
    __tablename__ = 'user_role'
    id = db.Column(db.Integer, primary_key=True)
    UserId = db.Column(db.ForeignKey(Support_User_Models.id))
    RoleId = db.Column(db.ForeignKey(Support_Role_Models.id))

    def to_json(self):
        json_data = {
            "id": self.UserId,
            "username": self.support_user.username,
            "roleName": self.support_role.roleName,
            "roleDesc": self.support_role.roleDesc
        }
        return json_data
