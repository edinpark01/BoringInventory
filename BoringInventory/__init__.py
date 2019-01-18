# Author:   Braulio Tonaco
# Date:     01/17/19
#
#   The __init__.py servers double duty:
#       1. It contains the application factory
#       2. It tells Python that the BoringInventory directory should be treated as a package
#
# ------------------------------------------------------------------------------------------------
#
#   This project direcotyr will contain:
#       BoringInventory/    a Python package containing our application code and files
#       Tests/              a directory containing test modules
#

import os

import click
from flask import Flask


def create_app(test_config=None):
    """ Creates and configures our Flask application - AKA "The application factory function" """

    click.echo(" * INITIALIZING APPLICATION FACTORY FUNCTION ")

    app = Flask(__name__, instance_relative_config=True)
    # __name__:
    #   It is the name of the current Python Module.
    #   The App needs to know where it's located to setup some paths, and __name__ is a convenient way to tell it.
    #
    # instance_relative_config=True:
    #   Tells the App that configuration files are relative to the "instance folder".
    #   The INSTANCE FOLDER is located outside our BoringInventory Package and can hold local data that should not be
    #   commited to version control, such as configuration secrets and the database file.

    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'inventory.sqlite')
    )
    # app_config.from_mapping():
    #   Sets some default configuration that the App will use:
    #       1. SECRET_KEY:
    #           It is used by Flask and extensions to keep data safe.
    #           It is set to 'dev' to provide a convenient value during development, BUT it should be overriden with
    #           random value when deploying.
    #       2. DATABASE:
    #           It is the path where the SQLite databse file will be saved.
    #           It is under app.instance_path, which is the path the Flask has chosen for the instance folder.

    if test_config is None:  # Loads the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
        # app.config.from_pyfile():
        #     Overrides the default configuration with values taken from the config.py file in the instance folder.
        #     For example: When deploying, this can be used to set a real SECRET_KEY.
        #
        # test_config:
        #     It can also be passed to the factory, and will be used instead of the instance configuration.
        #     This is so the tests we will write can be configured independently of any developement values we have
        #     configured.
    else:  # Load the test config if passed in
        app.config.from_mapping(test_config)

    try:  # Ensures the instance folder exists
        os.makedirs(app.instance_path)
        # os.makedirs():
        #   Ensures that app.instance_path exists.
        #   Flask does not create the instance folder automatically,BUT it needs to be created because our project
        #   will create a SQLite databse file there.
    except OSError:
        pass

    # @app.route():
    #   Creates a simple route so we can see the application working before getting the rest of the project developed.
    #   It creates a connection between the URL /hello and a function that returns a response.
    @app.route('/hello')
    def hello():
        """ A Simple page that says hello - To make sure our Flask App is running correctly """
        return 'Hello World'

    click.echo(" * Registering inventory's BluePrint with Flask Application ")
    from . import inventory
    app.register_blueprint(inventory.bp)

    click.echo(" * Registering db's BluePrint with Flask Application ")
    from . import db
    db.init_app(app)

    click.echo(" * RETURNING CREATED FLASK APP\n\n")

    return app
