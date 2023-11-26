import sys
import os.path
sys.path.append(os.path.dirname(sys.path[0]))

import psycopg2
import pandas as pd
from geopy.distance import distance as geodist
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from eta import ETAQuery  

load_dotenv()

app = Flask(__name__)

# Retrieve environment variables from .env file
DB_HOST = os.getenv("DATABASE_HOST")
DB_PORT = int(os.getenv("DATABASE_PORT"))
DB_NAME = os.getenv("DATABASE_NAME")
DB_USER = os.getenv("DATABASE_USER")
DB_PASSWORD = os.getenv("DATABASE_PASSWORD")

# DB connection
connection = psycopg2.connect(
    host=DB_HOST,
    port=DB_PORT,
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD
)

# Calculate_eta method requires that the new (lat, lon) position be inputted as json data -> eta appended to DB will be for all points in route.csv
@app.route('/calculate_eta', methods=['POST']) 
def calculate_eta():
    try:
        data = request.get_json()
        lat = data.get('lat')
        lon = data.get('lon')

        # Invalid lat or lon
        if lat is None or lon is None:
            return jsonify({'error': 'Invalid request data'}), 400

        eta_query = ETAQuery(lat, lon)
        eta_values = eta_query.get_times()

        # Insert a new row with lat, lon, and calculated eta (in mins)
        with connection.cursor() as cursor:
            # Find the maximum id in the table (ie. newest row) -> if no checkpoints, instantiate with 0
            cursor.execute("SELECT MAX(id) FROM public.checkpoints")
            max_id = cursor.fetchone()[0] or 0 

            # Insert the new row with an incremented id
            cursor.execute(
                "INSERT INTO public.checkpoints (id, lat, lon, eta) VALUES (%s, %s, %s, %s)",
                (max_id + 1, lat, lon, eta_values)
            )
            connection.commit()

        # Successful calculation and DB change
        return jsonify({'message': 'New row created with calculated ETA.', 'id': max_id + 1}), 200

    # Error message
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6000) 