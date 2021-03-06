import os

from flask_script import Manager, Server
from flask_migrate import MigrateCommand

from {{cookiecutter.project_name}} import create_app, db, migrate

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

manager.add_command('db', MigrateCommand)
manager.add_command('runserver', Server())

@manager.command
def createdb():
    """
    Creates a database
    """
    db.create_all()

if __name__ == '__main__':
    manager.run()
