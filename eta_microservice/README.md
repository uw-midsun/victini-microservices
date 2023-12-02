# ETA Microservice

A Flask microservice that updates the PostgreSQL database with the ETA (in mins) from the inputted point to the checkpoints in the checkpoint_model_db.csv file.

## Setup

### Python install

Install Python 3 on your system. To test, open a command prompt or a terminal and write `python3` or `py`.

### Project setup

Once Python is installed, clone this repo into your editor of choice.

Cloning the repository will create a new folder named `victini-microservices` with all the code -- you will have 'cloned' the repository!

Once cloned, run `cd victini-microservices/eta_microservice` to go into the new folder.

First, set up a virtual environment using `python3 -m venv`. This will create a `venv/` folder in your directory and isolate all of the porpject dependencies from other projects.

To source this environment run `source venv/bin/activate`.

Then, to install the project dependencies, run `pip install -r requirements.txt` -- this will install all the libraries listed in the `requirements.txt` file.

### Database Setup

To setup the database, run the SQL script found in the schemas folder to create the table. The table should have columns: id, lat, long and eta.

### Connection Setup

Once the DB is setup, navigate to the `.env` file and ensure that the DB connection details are correctly populated.

### Running the Microservice

After ensuring that you're in the `eta_microservice` folder and running your **virtual environment**, run `python main.py` to start the microservice.

The terminal should show that the Flask app is running on localhost on port 6000.

### Calculating ETA

With the microservice running, you can send a POST request for the `calculate_eta` function to run. 

Using tool like Postman, send a POST request like `http://localhost:6000/calculate_eta` and ensure that the **lat** and **long** and included in the **JSON** file:

eg. `{"lat": 43.46786317655638, "lon": -80.56637564010215}`

Update the checkpoints table to see the new point and the list of ETAs to each checkpoint.

If a checkpoint has already been passed or an error occurred while calculating the ETA, -1.0 will be the ETA.
