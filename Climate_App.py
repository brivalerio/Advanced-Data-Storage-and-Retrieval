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
        f"--Show precipitation for all days in entire dataset</br>"
        f"</br>"
        f"/api/v1.0/stations</br>"       
        f"--Show listing of all stations in dataset</br>"
        f"</br>"
        f"/api/v1.0/tobs</br>"
        f"--Shows temperature observations a year from the last data point</br>"
        f"</br>"
        f"/api/v1.0/'START-DATE-HERE'</br>"
        f"--Start date only: will calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date</br>"
        f"--Note: please input date as shown: '2016-04-01'</br>"
        f"--Example link: http://127.0.0.1:5000/api/v1.0/'2016-04-01'</br>"
        f"</br>"
        f"/api/v1.0/'START-DATE-HERE'/'END-DATE-HERE'</br>"
        f"--Start and end date: calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive</br>"
        f"--Note: please input dates as shown: '2016-04-01'</br>"
        f"--Example link: http://127.0.0.1:5000/api/v1.0/'2016-04-01'/'2016-04-13'</br>"
        )

if __name__ == '__main__':
    app.run(debug=True)