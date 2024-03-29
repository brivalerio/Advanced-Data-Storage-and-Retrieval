import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

# Setting up database
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()
# Reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

# "calc_temps" function
def calc_temps(start_date, end_date):
    """TMIN, TAVG, and TMAX for a list of dates.
    
    Args:
        start_date (string): A date string in the format %Y-%m-%d
        end_date (string): A date string in the format %Y-%m-%d
        
    Returns:
        TMIN, TAVE, and TMAX
    """
    
    return session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()

# Flask
app = Flask(__name__)

# Routes
@app.route("/")
def welcome():
    return(
        f"PLEASE READ: Paste the routes after the default browser link (Example: http://127.0.0.1:5000/api/v1.0/tobs)</br>"
        f"</br>"
        f"***AVAILABLE ROUTES***</br>"
        f"</br>"
        f"/api/v1.0/precipitation</br>"       
        f"--Show precipitation for all days in dataset range 2016-04-01 to 2017-03-31</br>"
        f"</br>"
        f"/api/v1.0/stations</br>"       
        f"--Show listing of all stations in dataset range 2016-04-01 to 2017-03-31</br>"
        f"</br>"
        f"/api/v1.0/tobs</br>"
        f"--Shows temperature observations in dataset range 2016-04-01 to 2017-03-31</br>"
        f"</br>"
        f"/api/v1.0/'START-DATE-HERE'</br>"
        f"--Start date only: will calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date to 2017-08-23 (last date in complete data range)</br>"
        f"--Note: please input date in format as shown: 'YYYY-MM-DD'</br>"
        f"--Example link: http://127.0.0.1:5000/api/v1.0/'2016-04-01'</br>"
        f"</br>"
        f"/api/v1.0/'START-DATE-HERE'/'END-DATE-HERE'</br>"
        f"--Start and end date: calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive</br>"
        f"--Note: please input date in format as shown: 'YYYY-MM-DD'</br>"
        f"--Example link: http://127.0.0.1:5000/api/v1.0/'2016-04-01'/'2016-04-13'</br>"
        )

@app.route("/api/v1.0/precipitation")
def precipitation():
    precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-04-01').\
        filter(Measurement.date <= '2017-03-31').order_by(Measurement.date).all()

    precip_total = []
    for p in precip:
        row = {"Date":p[0], "Precipitation":p[1]}
        precip_total.append(row)
        
    return jsonify(precip_total)

@app.route("/api/v1.0/stations")
def stations():
    stations = session.query(Station.station, Station.name).\
        join(Measurement, Station.station == Measurement.station).\
        filter(Measurement.date >= '2016-04-01').filter(Measurement.date <= '2017-03-31').\
        group_by(Station.station).all()
    
    station_list = []
    for s in stations:
        row = {"Station ID":s[0], "Station Name":s[1]}
        station_list.append(row)

    return jsonify(station_list)

@app.route("/api/v1.0/tobs")
def tobs():
    tobs = session.query(Measurement.date, Measurement.tobs).\
        filter(Measurement.date >= '2016-04-01').\
        filter(Measurement.date <= '2017-03-31').all()

    tobs_list = []
    for t in tobs:
        row = {"Date":t[0], "Temperature Observations (tobs)":t[1]}
        tobs_list.append(row)
    
    return jsonify(tobs_list)

@app.route("/api/v1.0/<start>")
def start_only(start):
    so_calc = calc_temps(start, '2017-08-23')
    for so in so_calc:
        row = {"TMIN":so_calc[0][0], "TAVG":so_calc[0][1], "TMAX":so_calc[0][2]}
    
    return jsonify(row)

@app.route("/api/v1.0/<start>/<end>")
def start_end(start,end):
    se_calc = calc_temps(start, end)
    for se in se_calc:
        row = {"TMIN":se_calc[0][0], "TAVG":se_calc[0][1], "TMAX":se_calc[0][2]}
    
    return jsonify(row)

if __name__ == '__main__':
    app.run(debug=False)