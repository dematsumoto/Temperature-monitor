# TEMPERATURE MONITOR #

### What is this repository for? ###

* This is a web application for personal use. The purpose of this project is to use a Raspberry Pi to collect data from real word (temperature sensor, I/O states) and display it through a web browser.
* The data are gathered using a Raspberry Pi and stored into a SQLite database. The Restful web service, then, provides the controllers and views for the user to access the data and Charts of the sensors. 


### How do I set up? ###

* The project was developed in Python using [Flask](http://flask.pocoo.org/) and [Sqlite3](https://www.sqlite.org/index.html). Python at least 3.4 is required to build the application.
* Virtual Environment should be used to run the poject. Python 3 comes bundled with the [venv](https://docs.python.org/3/library/venv.html#module-venv) module to create virtual environments.
* How to setup the application: First clone this repo. At the project root directory, execute from the command line the command below to create an environment:
```
python3 -m venv venv
```
Activate the environment:
```
. venv/bin/activate
```
Install dependencies and the flask application
```
pip install -r requirements.txt
pip install -e .
```
To start the application:
```
export FLASK_APP=flaskr
export FLASK_ENV=development
```
If you are running the application within the Raspebrry Pi you should inform the application:
```
export RPI_SUPPORTED=true
``` 
Now initialize the DB, this command is only needed to create the DB files on the first time to setup the database (it will destroy any existing DB files and create new ones)
```
flask init-db
```
Running the Application:
```
flask run
```
The application will start at `http://localhost:5000`

* Some screenshots from the application: [Login Screen](https://raw.githubusercontent.com/dematsumoto/dematsumoto.github.io/master/images/temp_monitor_demo/chart.png), [Temperature Readings](https://raw.githubusercontent.com/dematsumoto/dematsumoto.github.io/master/images/temp_monitor_demo/dashobard.png), [Device Manager](https://raw.githubusercontent.com/dematsumoto/dematsumoto.github.io/master/images/temp_monitor_demo/device_manager.png), [Chart](https://raw.githubusercontent.com/dematsumoto/dematsumoto.github.io/master/images/temp_monitor_demo/chart.png)
