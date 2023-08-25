**SOLUTION: Fixing of flask app running method: app.py**

To fix the flask app, app.py running in shell, we have changed the running of the flask app from shell execution to a service type execution.
Running a python script as a service involves setting up the app.py script to run continuously in the background.

So to do that first we made a configuration file "response.service": which is going to execute the app.py script 
at certain frequency. 
Here we have set it to 5sec, so the the server response is available almost always while preventing multiple restarts too frequently 
which can cause start-limit-hit failure. 

Lastly the response service is enabled and started, making the web servers available for response to requests
until they are manually stopped or unless the server is stopped.
