# import the Flask class from the flask module
from flask import Flask, render_template, request, url_for
from launchpad_reports import created_bugs
from tabulate import tabulate

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def index():
    return render_template('index.html')

# This will generate the index and save the input data + create a table for printing on /report
@app.route('/report', methods=['POST'])
def report():
    usernames = request.form['usernames']
    start_date = request.form['date']
    filtered_bugs = {}
    bug_table = []
    for user in usernames.split():
        filtered_bugs[user] = created_bugs(user, start_date)
        bug_count = 0 
        for bug in filtered_bugs[user]:
            bug_count = bug_count + 1 
            bug_table.append([bug_count, user, bug.status, bug.date_created.strftime("%Y-%m-%d"), bug.web_link])
    return render_template('report.html', bug_table=bug_table)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)

