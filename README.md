# launchpad-reports-flask

## Pre-Built Docker Image: docker pull mpetason/launchpad_reports

The prebuilt docker image will let you download and then run the container without building it locally.

`docker run -d --name launchpad_reports -p 8001:8001 mpetason/launchpad-reports-flask:latest`

## Flask + Launchpad Reports

Install Requirements: `pip install -r requirements.txt`

Run Application: `python app.py`

Default : http://0.0.0.0:8001

The WebUI will allow you to enter in users, separated by commas, and a start date. The start date will look for bugs between the start date and todays date. 

A Dockerfile has been included in case you want to modify and create an image from scratch. The default bind host and port are: 0.0.0.0:8001, which may conflict with already running applications. To modify this you can edit app.py and change where the server binds. If you are building a docker image - make sure you update the docker run commands.  

To create docker image: `docker build -t launchpad_reports_flask:latest .`

To run container: `docker run -d --name launchpad_reports -p 8001:8001 launchpad_reports_flask`
