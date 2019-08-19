#!/usr/bin/env python
#_*_ coding:utf-8 _*_

from roles import db
from .User import Support_Permission_Models, Support_Menu_Models

class SUP_Permission_Menu_Model(db.Model):
    """Permission And menu Link"""
    __tablename__ = 'permission_menu'

    id = db.Column(db.Integer, primary_key=True)
    permissionId = db.Column(db.ForeignKey(Support_Permission_Models.id))
    menuId = db.Column(db.ForeignKey(Support_Menu_Models.id))