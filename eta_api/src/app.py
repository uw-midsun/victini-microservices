import os
from flask import Flask, request, jsonify
from eta_api.src.eta import ETAQuery  # Import the ETAQuery class from eta.py
from eta_api.src.models import db, User  # Import the db and User models from models.py
from flask_migrate import Migrate

# Initialize Flask app
app = Flask(__name__)

# Configuration
app.config.from_object(os.environ['APP_SETTINGS'])
db.init_app(app)
migrate = Migrate(app, db)

# Define routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        lat = float(request.form['lat'])
        lon = float(request.form['lon'])

        # Calculate ETA using ETAQuery
        eta_query = ETAQuery(lat, lon)
        times = eta_query.get_times()

        # Return ETA as JSON
        return jsonify({'eta': times})

    return 'Welcome to the ETA Service'

@app.route('/users', methods=['POST'])
def create_user():
    name = request.json.get('name')
    if name:
        user = User(name=name)
        db.session.add(user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})
    else:
        return jsonify({'error': 'Name is required'}), 400

if __name__ == '__main__':
    app.run()
