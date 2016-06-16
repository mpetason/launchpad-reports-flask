# import the Flask class from the flask module
from flask import Flask, render_template, request, url_for
from launchpad_report import created_bugs
from tabulate import tabulate

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def hello():
    return render_template('index.html')

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
            bug_table.append([bug_count, user, bug.web_link])
    #bug_table = tabulate(bug_table, headers=["#", "Username", "Bug URL"], tablefmt="psql", numalign="left")
    return render_template('report.html', bug_table=bug_table)



# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)

