import functools

import click
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from BoringInventory.db import get_db

from werkzeug.exceptions import abort

bp = Blueprint('inventory', __name__)


@bp.route('/')
def index():

    click.echo(" * Executing index() from inventory.py")

    db = get_db()

    data = db.execute(
        'SELECT c.* FROM cabinets c '
        'JOIN cabinet_info c_i '
        'ON c.cabinet = c_i.id '
        'ORDER BY c.cabinet ASC'
    ).fetchall()

    return render_template('inventory/index.html', data=data)


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
def update(id):

    click.echo(" * Executing update() from inventory.py")

    db = get_db()

    data = db.execute(
        'SELECT * FROM cabinets c '
        'WHERE c.rowid = ? ', (id,)
    ).fetchone()

    if request.method == 'POST':
        print(request.form)
        print(type(request.form))

    click.echo(" * Executing update() from inventory.py")

    return render_template('inventory/update.html', id=id, data=data)

