from flask import (
    Blueprint, render_template
)

from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr.raspberry.temp_reader import measure_temp

bp = Blueprint('dashboard', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()
    temperatures = db.execute(
        'SELECT t.id, t.sensor_reading, d.description, t.created'
        ' FROM temperature t JOIN device d ON t.device_id = d.id'
        ' JOIN user u ON u.id = d.owner_id'
    ).fetchall()

    return render_template('dashboard/index.html', temperatures=temperatures)

