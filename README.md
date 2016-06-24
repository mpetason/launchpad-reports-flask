# launchpad-reports-flask

## Pre-Built Docker Image: docker pull mpetason/launchpad_reports

Flask + Launchpad Reports

Install Requirements: `pip install -r requirements.txt`

Run Application: `python app.py`

Default : http://0.0.0.0:8001

A Dockerfile has been included in case you want to modify and create an image from scratch. The default bind host and port are: 0.0.0.0:8001, which may conflict with already running applications. To modify this you can edit app.py and change where the server binds. 

To create docker image: `docker build -t launchpad_reports_flask:latest .`

To run container: `docker run -d -p 8001:8001 launchpad_reports_flask`
