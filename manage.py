from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Server, Command
from flask_migrate import Migrate, MigrateCommand

# ---------------------------------------------------------------------------------
# Create an Application Object
# ---------------------------------------------------------------------------------
# The following line of code initializes the Flask application object to be
# used throughout the rest of the application
#

app = Flask(__name__)

# ---------------------------------------------------------------------------------
# Set Development Environment Configuration
# ---------------------------------------------------------------------------------
# The following line of code initializes the configuration variables needed
# to run the app in Localhost, Development, Staging & Production
# environments. To change the configurations see config.py
#

app.config.from_object('config.LocalhostConfig')


@app.route("/", methods=('GET', 'POST'))
def index():
    return 'Time to get building!'

# ---------------------------------------------------------------------------------
# Connect to the Database
# ---------------------------------------------------------------------------------
# The following lines of code:
#
# Create an instance of the database connection
# Import all the database models from models.py
# Configure the Flask-Migrate migration manager
#

db = SQLAlchemy(app)

from models import *

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def runserver():
    app.run(debug=True, host="0.0.0.0", port=5000)

if __name__ == "__main__":
    manager.run()
