import os
from flask import Flask, request, jsonify
from . import create_app, db
from .models import ETA

app = create_app(os.getenv("FLASK_ENV"))

@app.route("/add_eta", methods=["POST"])
def add_eta():
    data = request.get_json()
    lat = data.get("lat")
    long = data.get("long")
    eta = data.get("eta")

    if lat is None or long is None or eta is None:
        return jsonify({"error": "Invalid data"}), 400

    eta_entry = ETA(lat=lat, long=long, eta=eta)
    db.session.add(eta_entry)
    db.session.commit()

    return jsonify({"message": "ETA added successfully"}), 201

@app.route("/get_eta", methods=["GET"])
def get_eta():
    etas = ETA.query.all()
    eta_list = [{"lat": eta.lat, "long": eta.long, "eta": eta.eta} for eta in etas]
    return jsonify({"etas": eta_list})

if __name__ == "__main__":
    app.run()
