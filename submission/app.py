# Dependencies.
# SQL Alchemy
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func, text

# Flask
from flask import Flask, jsonify

# Other.
import datetime as dt
from time import sleep
import os
os.chdir(os.path.dirname(os.path.realpath(__file__)))


# Database Setup...
# Create engine using the `hawaii.sqlite` database file.
filepath = "../data/hawaii.sqlite"
engine = create_engine(f"sqlite:///{filepath}")

# Declare a Base using `automap_base()`.
Base = automap_base()

# Use the Base class to reflect the database tables.
Base.prepare(autoload_with = engine)

# Print all of the classes mapped to the Base.
Base.classes.keys()

# Assign the classes as follows...
# 'Measurement' = measurement class.
# 'Station' = station class.
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create a session.
session = Session(engine)



# Functions...
# Find the most recent point of data in the database.
def get_latest():
    latest = session.query(
        func.max(Measurement.date)
    ).all()

    latest = dt.datetime.strptime(latest[0][0], "%Y-%m-%d")
    sleep(1)
    return latest

# Get the most active station in the database.
def get_active():
    results = session.query(
        Measurement.station,
        Station.name,
        func.count(Measurement.station)
    ).group_by(Measurement.station
    ).filter(Station.station == Measurement.station
    ).order_by(func.count(Measurement.station).desc()
    ).all()

    return results[0]

# Flask Setup
app = Flask(__name__)



# Flask Routes...
# Index - lists all available routes.
@app.route("/")
def index():
    return (
        f"Welcome to the Hawaii Weather API.<br/>"
        f"<br/>Available routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start_date<br/>"
        f"/api/v1.0/start_date/end_date<br/>"
        f"<br/>Note: dates formatted as YYYY-DD-MM.<br/>"
    )

# Precipitation - returns the past 12 months of data as a JSON.
@app.route("/api/v1.0/precipitation")
def precipitation():
    latest = get_latest()

    # Query for the past 12 months of data.
    data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= (latest - dt.timedelta(days = 365))).all()
    
    # Convert the results of the query to a dict.
    result = dict()
    for item in data:
        result[item[0]] = item[1]

    # Return the result as a JSON.
    return jsonify(result)

# Stations - returns a list of stations as a JSON.
@app.route("/api/v1.0/stations")
def stations():
    data = session.query(
        Station.station,
        Station.name
    ).all()

    # Convert the results to a dict.
    result = dict()
    for item in data:
        result[item[0]] = item[1]

    return jsonify(result)

# Tobs - returns the past year of data for the most active station as a JSON.
@app.route("/api/v1.0/tobs")
def tobs():
    latest = get_latest()
    active = get_active()

    data = session.query(
        Measurement.date,
        Measurement.tobs
    ).filter(Measurement.station == active[0]
    ).filter(Measurement.date >= (latest - dt.timedelta(days = 365))
    ).all()

    # Convert the results to a dict.
    result = dict()
    for item in data:
        result[item[0]] = item[1]

    return jsonify(result)

# Custom (with start) - returns precipitation statistics starting at the date as a JSON.
@app.route("/api/v1.0/<start_date>")
def s_tobs(start_date):
    try:
        s_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
        data = session.query(
            func.min(Measurement.tobs),
            func.max(Measurement.tobs),
            func.avg(Measurement.tobs)
        ).filter(Measurement.date >= s_date
        ).all()

        # Convert the results to a dict.
        result = dict()
        for item in data:
            result['min'] = item[0]
            result['max'] = item[1]
            result['avg'] = item[2]

        return jsonify(result)
    
    except:
        return (
            f"Invalid date entered: {start_date}.<br/>"
            f"The format should be: YYYY-MM-DD<br/>"
            f"Example: 2014-04-25<br/>"
        )
    
    return None

# Custom (with start/end) - returns precipitation statistics within the range specified as a JSON.
@app.route("/api/v1.0/<start_date>/<end_date>")
def se_tobs(start_date, end_date):
    try:
        s_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
        e_date = dt.datetime.strptime(end_date, "%Y-%m-%d")

        data = session.query(
            func.min(Measurement.tobs),
            func.max(Measurement.tobs),
            func.avg(Measurement.tobs)
        ).filter(Measurement.date >= s_date
        ).filter(Measurement.date <= e_date
        ).all()

        # Convert the results to a dict.
        result = dict()
        for item in data:
            result['min'] = item[0]
            result['max'] = item[1]
            result['avg'] = item[2]

        return jsonify(result)
    
    except:
        return (
            f"Invalid dates entered: {start_date} : {end_date}.<br/>"
            f"The format should be: YYYY-MM-DD<br/>"
            f"Example: 2014-04-25<br/>"
        )
    
    return None

# Start the page.
if __name__ == "__main__":
    app.run(debug=True)