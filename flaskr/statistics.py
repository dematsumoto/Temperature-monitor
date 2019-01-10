from flask import (
    Blueprint, render_template, g, request, flash, redirect, url_for, abort
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
    data = db.execute(
        'SELECT sensor_reading, created FROM temperature'
        ' WHERE device_id = ?', (id,)
    ).fetchall()

    return data