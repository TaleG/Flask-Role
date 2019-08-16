#!/usr/bin/env python
#_*_ coding:utf-8 _*_


from roles import Create_App, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_cors import CORS

app = Create_App("develop")
CORS(app)

manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)

if __name__ == '__main__':
    manager.run()
