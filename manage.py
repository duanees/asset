#/usr/bin/env python
import os
import sys
from flask.ext.migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db
from app.db.models import User, ActionView

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

app=create_app(os.getenv('FLASK_CONFIG') or 'default')
manager =Manager(app)
migrate = Migrate(app, db)

def make_shell_context():
    return dict(app=app, db=db, User=User, Action=ActionView)
manager.add_command('shell',Shell(make_context=make_shell_context))
manager.add_command('db',MigrateCommand)

if __name__ == '__main__':
    # manager.run()
    app.run()
