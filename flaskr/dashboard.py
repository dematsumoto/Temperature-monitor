from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('dashboard', __name__)


@bp.route('/')
@login_required
def index():
    db = get_db()
    temperatures = db.execute(
        'SELECT id, sensor_reading, description, created'
        ' FROM temperature  WHERE owner_id = ?', (g.user['id'],)
    ).fetchall()

    return render_template('dashboard/index.html', temperatures=temperatures)
