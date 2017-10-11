from launchpadlib.launchpad import Launchpad
from datetime import timedelta, datetime
from tabulate import tabulate
import argparse

cachedir = ".launchpadlib/cache/"
launchpad = Launchpad.login_anonymously('just testing', 'production', 
                                        cachedir, version='devel')

# Created_bugs will query launchpad for bugs created by the speicified user.
def created_bugs(user, start_date):
    lp_user = launchpad.people(user)
    return lp_user.searchTasks(owner=lp_user,created_since=start_date,status=[
                   "New","Opinion","Invalid","Won't Fix","Expired","Confirmed",
                   "Triaged", "In Progress","Fix Committed","Fix Released",
                   "Incomplete (with response)","Incomplete (without response)"
                   ])

# CLI setup to allow for CLI usage with specified flags.
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Launchpad Bug Reports per '
                                     'User')
    parser.add_argument('-u', '--usernames', nargs="+",
                        help = 'enter usernames in comma separated format.',
                        required = True)
    parser.add_argument('-d', '--days', help = 'number of days to go back.',
                        type=int)
    parser.add_argument('-a', '--after',
                        help = 'Search for bugs created After this date. '
                        'Date is in Y-M-D format')
    args = parser.parse_args()

# Pull start date based on which value was entered.
    if not args.after:
        start_date = datetime.today() - timedelta(days=args.days)
    else:
        start_date = args.after
    filtered_bugs = {}
    bug_table = []
    for user in args.usernames[0].split(','):
        filtered_bugs[user] = created_bugs(user, start_date)
        bug_count = 0
        for bug in filtered_bugs[user]:
            bug_count += 1
            bug_table.append([bug_count, user, bug.status,
                             bug.date_created.strftime("%Y-%m-%d"),
                             bug.web_link])

# Print out content in an easy to read format - psql.
    print(tabulate(bug_table, headers=["#", "Username", "Status",
                                       "Date Created", "Bug URL"],
                                       tablefmt="psql", numalign="left"))
