import os
import sqlite3


def measure_temp():
    temp = _get_temp()
    _save_to_db(temp)


def _get_temp():
    is_compatible = False  #in case this code run outside UNIX systems

    temp = 'temp=61.9ºC' if not is_compatible else os.popen("vcgencmd measure_temp").readline()
    temp = temp.replace("ºC", "")
    return temp.replace("temp=", "")


def _get_db():
    conn = sqlite3.connect('instance/flaskr.sqlite')
    return conn, conn.cursor()


def _save_to_db(temp):
    conn, db = _get_db()
    db.execute(
        'INSERT INTO temperature (device_id, sensor_reading, created)' 
        ' VALUES (1, ?, DATETIME(\'NOW\'))', (temp,)
    )
    conn.commit()
    conn.close()
