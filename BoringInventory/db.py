import sqlite3
import click

from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

# g:
#   g is a special object that is unique for each request. It is used to store data that might be accessed by multiple
#   functions during the request.
#   The connection is stored and reused instead of creating a new connection if get_db is called a second time in
#   the same request.
#
# current_app:
#   This is another special object that points to the Flask application handling the request. Since we are using an
#   application factory, there is no application object when writing the rest of our code.
#   get_db will be called when the application has been created and is handling a request, so current_app can be
#   used.
#
# sqlite3.connect():
#   Extablishes a connection to the file pointed at by the DATABASE configuration key.


def close_db(e=None):
    """ Checks if a connection was created by checking if g.db is set.
        This function is used in the application factory after each request """
    db = g.pop('db', None)

    if db is not None:
        db.close()
