import os
import sqlite3


def measure_temp():
    temp = _get_temp()
    _save_to_db(temp)


def _get_temp():
    # is_compatible = False  #in case this code run outside UNIX systems

    rpi_supported = os.environ.get('RPI_SUPPORTED', 'False')
    is_compatible = True if rpi_supported.lower() == 'true' else False

    temp = "temp=61.9'C" if not is_compatible else os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("'C", "")
    return temp.replace("temp=", "")


def _get_db():
    conn = sqlite3.connect('instance/flaskr.sqlite')
    return conn, conn.cursor()


def _save_to_db(temp):
    conn, db = _get_db()
    db.execute(
        'INSERT INTO temperature (device_id, sensor_reading, created)' 
        ' VALUES (555, ?, DATETIME(\'NOW\'))', (temp,)
    )
    conn.commit()
    conn.close()
