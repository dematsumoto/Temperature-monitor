import atexit
from flaskr import temp_reader

from apscheduler.schedulers.background import BackgroundScheduler


def get_temp():
    temp_reader.measure_temp()


def start_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(func=get_temp, trigger="interval", seconds=3)
    scheduler.start()
    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())
