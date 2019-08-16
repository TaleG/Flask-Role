#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from roles import db
from .User import Support_Permission_Models, Support_Role_Models

class Permission_Role_Models(db.Model):
    """ Role And Permission Link"""

    __tablename__ = 'permission_role'
    id = db.Column(db.Integer, primary_key=True)
    permissionId = db.Column(db.ForeignKey(Support_Permission_Models.id))
    roleId = db.Column(db.ForeignKey(Support_Role_Models.id))
