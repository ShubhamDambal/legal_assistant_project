import sqlite3
from flask import current_app, g

def get_db():
    """Opens a database connection and returns the connection object."""
    if 'db' not in g:
        g.db = sqlite3.connect(
            'legal_assistant.db',  # Replace with your database name
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    """Closes the database connection if it exists."""
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_app(app):
    """Registers the database functions with the Flask app."""
    app.teardown_appcontext(close_db)
