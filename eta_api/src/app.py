from flask import Flask, render_template, request
from models import ETAQuery

# When the database models are defined, the following line will import it
# from modles import db

# App Initialization
app = Flask(__name__)

# Routes/logics here
@app.route("/", methods=["GET", "POST"])
def eta():
    if request.method == "POST":
        lat = float(request.form["lat"])
        lon = float(request.form["lon"])
        eta_query = ETAQuery(lat, lon)
        times = eta_query.get_times()
        return render_template("result.html", times=times)
    return render_template("index.html")


# Start server, currently this is only meant to work on a local server
if __name__ == "__main__":
    # To Run the Server in Terminal => flask run -h localhost -p 5000
    # To Run the Server with Automatic Restart When Changes Occurred => FLASK_DEBUG=1 flask run -h localhost -p 5000
    app.run()

# For when the server is ready, it can be configured here using the following code
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8080)
