# This file will be heavily dependent on your service but some general steps are detailed below

# Ensure that any dependencies (eg. libraries, packages, files, DB) are accounted for here

# Retrieve environment variables (ie. DB credentials) and connect to your DB

# Write your API methods/endpoints below as needed (this should take care of pulling data and writing it as needed through the use of JSON data)

# Your API method can most likely pull the necessary data, feed it into your logic/other python file (eg. for the ETA API, it feeds the data into the eta.py file, and execute the appropriate methods

# Below is the code needed to start running your microservice -> The code below will run your microservice locally on port 6000 (change as necessary if it's already taken)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000) 