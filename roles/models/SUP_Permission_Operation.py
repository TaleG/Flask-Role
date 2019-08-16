#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from roles import db
from .User import Support_Permission_Models, Support_Operation_Models

class SUP_Permission_Operation_Models(db.Model):
    """Permission Link Table"""
    __tablename__ = "permission_operation"
    id = db.Column(db.Integer, primary_key=True)
    PermissionId = db.Column(db.ForeignKey(Support_Permission_Models.id))
    OperationID = db.Column(db.ForeignKey(Support_Operation_Models.id))



