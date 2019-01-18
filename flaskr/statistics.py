from flask import (
    Blueprint, render_template, g, request, flash, redirect, url_for, abort, current_app
)

from flaskr.auth import login_required
from flaskr.db import get_db


bp = Blueprint('statistics', __name__)


@bp.route('/stats')
@login_required
def statistics():
    return render_template('dashboard/statistics.html', devices=_get_devices(), option=None)


@bp.route('/stats/device/', methods=['GET'])
@login_required
def get_data():
    device_id = request.args.get('deviceId')
    current_app.logger.info(device_id)
    db = get_db()
    data = db.execute(
        'SELECT id, created, sensor_reading FROM temperature'
        ' WHERE device_id = ?'
        'LIMIT 50', (device_id,)
    ).fetchall()

    # for row in cursor:
    #     data.append(list(row))

    # return None  # render_template('dashboard/stats_pie_chart.html', data=cursor)

    return render_template('dashboard/stats_pie_chart.html',
                           devices=_get_devices(),
                           data=data,
                           option=device_id)


def _get_devices():
    db = get_db()
    devices = db.execute(
        'SELECT id, description FROM device'
        ' WHERE owner_id = ?', (g.user['id'],)
    ).fetchall()

    return devices


def _get_device_index(devices_list, id):
    # devices_list = []
    # for device in devices:
    #     devices_list.append(list(device))

    return [ind for ind in range(len(devices_list)) if id in devices_list[ind]]

