from flask import Flask, render_template, request, Response
from launchpad_reports import created_bugs
from tabulate import tabulate
from datetime import datetime
from io import BytesIO
import csv

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def index():
    return render_template('index.html')

# get bugs from created_bugs and then format the output into a table for
# printing on /report
@app.route('/report', methods=['POST'])
def report():
    usernames = request.form['usernames']
    start_date = request.form['date']
    filtered_bugs = {}
    bug_table = []

    for user in usernames.split(','):
        filtered_bugs[user] = created_bugs(user, start_date)
        bug_count = 0
        for bug in filtered_bugs[user]:
            bug_count = bug_count + 1
            bug_table.append([bug_count, user, bug.status,
                             bug.date_created.strftime("%Y-%m-%d"),
                             bug.web_link])
    return render_template('report.html', usernames=usernames,
                            start_date=start_date, bug_table=bug_table)

# Creates a CSV file that will match the output on the page.
@app.route('/genCSV')
def genCSV():
    usernames = request.args.get('usernames')
    start_date = request.args.get('start_date')
    filtered_bugs = {}
    bug_csv = []
    output = BytesIO()
    writer = csv.writer(output)

    for user in usernames.split(','):
        filtered_bugs[user] = created_bugs(user, start_date)
        bug_count = 0
        for bug in filtered_bugs[user]:
            bug_count = bug_count + 1
            bug_csv.append([bug_count, user, bug.status,
                            bug.date_created.strftime("%Y-%m-%d"),
                            bug.web_link])
    writer.writerow(['Bug Count', 'User', 'Status', 'Creation Date', 'Link'])
    writer.writerows(bug_csv)
    csv_filename = "Launchpad_Reports-" + str(datetime.today()) + ".csv"

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition":
                "attachment; filename=%s" % csv_filename})

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)

