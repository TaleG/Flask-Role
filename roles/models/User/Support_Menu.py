#!/usr/bin/env python
#_*_ coding:utf-8 _*_
from roles import db

class Support_Menu_Models(db.Model):
    """Menu List"""
    __tablename__ = 'support_menu'

    id = db.Column(db.Integer, primary_key=True)
    parentId = db.Column(db.Integer)
    menuName = db.Column(db.String(32))
    menuIcon = db.Column(db.String(128))
    menuUrl = db.Column(db.String(128))
    menuType = db.Column(db.Integer)
    menuOrder = db.Column(db.Integer)
    menuStatus = db.Column(db.Boolean)
    menu_List = db.relationship('SUP_Permission_Menu_Model',
                                backref="support_menu", lazy='dynamic')


    def to_json(self):
        json_data = {
            "menuId": self.id,
            "parentId": self.parentId,
            "menuName": self.menuName,
            "menuIcon": self.menuIcon,
            "menuUrl": self.menuUrl,
            "menuType": self.menuType,
            "menuOrder": self.menuOrder,
            "menuStatus": self.menuStatus
        }
        return json_data