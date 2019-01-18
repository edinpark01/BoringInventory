import functools

from flask import ( Blueprint, flash, g, redirect, render_template, request, url_for )


# TODO: Develop auth.py file
#from BoringInventory.auth import login_required

# TODO: Develop db.py file
#from BoringInventory.db import get_db

from werkzeug.exceptions import abort


bp = Blueprint('inventory', __name__)


@bp.route('/')
def index():
    return render_template('inventory/index.html')

