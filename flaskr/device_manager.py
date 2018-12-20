from flask import (
    Blueprint, render_template, g, request, flash, redirect, url_for, abort
)

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('devices', __name__)


@bp.route('/devices')
@login_required
def device_manager():
    db = get_db()
    devices = db.execute(
        'SELECT id, description FROM device'
        ' WHERE owner_id = ?', (g.user['id'],)
    ).fetchall()

    return render_template('dashboard/device_manager.html', devices=devices)


@bp.route('/add_device', methods=('GET', 'POST'))
@login_required
def add_device():
    if request.method == 'POST':
        device_id = request.form['device_id']
        description = request.form['description']
        error = None

        if not device_id:
            error = 'Device ID is required.'

        if not description:
            error = 'Description is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO device (id, owner_id, description)'
                ' VALUES (?, ?, ?)',
                (device_id, g.user['id'], description)
            )
            db.commit()
            return redirect(url_for('devices.device_manager'))

    return render_template('dashboard/device_manager.html')


def get_device(id):
    device = get_db().execute(
        'SELECT id, owner_id FROM device'
        ' WHERE id = ?', (id,)
    ).fetchone()

    if device is None:
        abort(404, "Device id {0} doesn't exist.".format(id))

    if device['owner_id'] != g.user['id']:
        abort(403)

    return device


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_device(id)
    db = get_db()
    db.execute('DELETE FROM device WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('devices.device_manager'))
