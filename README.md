# launchpad-reports-flask
Flask + Launchpad Reports

Install Requirements: pip install -r requirements.txt

Run Application: python app.py

Default : http://0.0.0.0:8001

Dockerfile included. 

To create docker image: `docker build -t launchpad_reports_flask:latest .`

To run container: `docker run -d -p 8001:8001 launchpad_reports_flask`
