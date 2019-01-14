from flask import (
    Blueprint, render_template, g, request, flash, redirect, url_for, abort, current_app
)

from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('statistics', __name__)


@bp.route('/stats')
@login_required
def statistics():
    db = get_db()
    devices = db.execute(
        'SELECT id, description FROM device'
        ' WHERE owner_id = ?', (g.user['id'],)
    ).fetchall()

    return render_template('dashboard/statistics.html', devices=devices)


@bp.route('/<int:id>/stats')
@login_required
def get_data(id):

    db = get_db()
    data = []
    cursor = db.execute(
        'SELECT sensor_reading, created FROM temperature'
        ' WHERE device_id = ?'
        'LIMIT 50', (id,)
    ).fetchall()

    # for row in cursor:
    #     data.append(list(row))

    return cursor
