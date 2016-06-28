Docker
######################################################################################################################################
The Docker repository hosting this is mpetason/launchpad_reports

The default WebUI will listen on 8001. This can be modified in the app.py if needed. 

Docker Pull 
docker pull mpetason/launchpad_reports

Docker Images
mpetason/launchpad_reports   latest              374044c41bdf        24 hours ago        440.5 MB

Docker Run
docker run -d --name launchpad -p 8001:8001 mpetason/launchpad_reports:latest

If the image has been updated then you can kill the currently running container
docker kill launchpad
docker rm launchpad

Then re-run Pull and re-run Run. Which will give you a new container with the new image. 
######################################################################################################################################

WebUI
######################################################################################################################################
The WebUI will be located at {ip}:8001. Within the WebUI you can get the same functionality as the -u and -a flags allow in the script. 
There is also an option to download the output as a .csv file. 

http://0.0.0.0:8001 (default listening location so it will bind anywhere)
######################################################################################################################################

CLI
######################################################################################################################################
Examples of how to use the CLI via the Container

-u, --usernames - Enter in Usernames comma separated
-a, --after - Date in Y-M-D. Search for bugs created after this date.
-d, --days - Search bugs created in the last X days. IE '-d 90'.

Running the Command with usernames in line

Command
docker exec launchpad python launchpad_reports.py -u mpetason,smachtmes -a 2016-01-01

Output
+-----+------------+---------------+----------------+----------------------------------------------+
| #   | Username   | Status        | Date Created   | Bug URL                                      |
|-----+------------+---------------+----------------+----------------------------------------------|
| 1   | mpetason   | Confirmed     | 2016-01-19     | https://bugs.launchpad.net/fuel/+bug/1535831 |
| 2   | mpetason   | Confirmed     | 2016-01-19     | https://bugs.launchpad.net/fuel/+bug/1535912 |
| 1   | smachtmes  | Fix Committed | 2016-04-04     | https://bugs.launchpad.net/fuel/+bug/1566017 |
| 2   | smachtmes  | Confirmed     | 2016-04-08     | https://bugs.launchpad.net/fuel/+bug/1568058 |
| 3   | smachtmes  | Fix Committed | 2016-04-19     | https://bugs.launchpad.net/fuel/+bug/1572296 |
+-----+------------+---------------+----------------+----------------------------------------------+

Running the Command with a For loop for usernames

Command
for user in {mpetason,smachtmes}; do docker exec launchpad python launchpad_reports.py -u $user -a 2015-01-01;done

Output
+-----+------------+--------------+----------------+----------------------------------------------+
| #   | Username   | Status       | Date Created   | Bug URL                                      |
|-----+------------+--------------+----------------+----------------------------------------------|
| 1   | mpetason   | Fix Released | 2015-10-07     | https://bugs.launchpad.net/fuel/+bug/1503753 |
| 2   | mpetason   | Confirmed    | 2016-01-19     | https://bugs.launchpad.net/fuel/+bug/1535831 |
| 3   | mpetason   | Confirmed    | 2016-01-19     | https://bugs.launchpad.net/fuel/+bug/1535912 |
+-----+------------+--------------+----------------+----------------------------------------------+
+-----+------------+---------------+----------------+----------------------------------------------------------------+
| #   | Username   | Status        | Date Created   | Bug URL                                                        |
|-----+------------+---------------+----------------+----------------------------------------------------------------|
| 1   | smachtmes  | Fix Released  | 2015-01-23     | https://bugs.launchpad.net/fuel/+bug/1413816                   |
| 2   | smachtmes  | Fix Released  | 2015-08-27     | https://bugs.launchpad.net/fuel/+bug/1489625                   |
| 3   | smachtmes  | Fix Released  | 2015-08-27     | https://bugs.launchpad.net/fuel/+bug/1489629                   |
| 4   | smachtmes  | Fix Released  | 2015-11-24     | https://bugs.launchpad.net/python-openstackclient/+bug/1519132 |
| 5   | smachtmes  | Fix Committed | 2016-04-04     | https://bugs.launchpad.net/fuel/+bug/1566017                   |
| 6   | smachtmes  | Confirmed     | 2016-04-08     | https://bugs.launchpad.net/fuel/+bug/1568058                   |
| 7   | smachtmes  | Fix Committed | 2016-04-19     | https://bugs.launchpad.net/fuel/+bug/1572296                   |
+-----+------------+---------------+----------------+----------------------------------------------------------------+
#####################################################################################################################################

