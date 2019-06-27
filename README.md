# Advanced-Data-Storage-and-Retrieval
</br>
For this excerise, we're taking a vacation to Honolul, Hawaii! To help with our trip planning before we leave, we need to do some climate analysis on the area.  There are 2 steps we need to complete in order to do so.</br>

## Step 1 - Climate Analysis and Exploration</br>
To begin, we used Python and SQLAlchemy to do basic climate analysis and data exploration of the provided climate database. All of the following analysis were completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.</br>
</br>
-Use the provided starter notebook and hawaii.sqlite files to complete your climate analysis and data exploration.</br>
-Choose a start date and end date for your trip. Make sure that your vacation range is approximately 3-15 days total.</br>
-Use SQLAlchemy create_engine to connect to your sqlite database.</br>
-Use SQLAlchemy automap_base() to reflect your tables into classes and save a reference to those classes called Station and Measurement.</br>
### Precipitation Analysis</br>
-A query was designed to pull the last 12 months of data based on the first day of vacation.</br>
-The results were then loaded into a Pandas Dataframe.</br>
-We then plotted the results using Matplotlib.</br>
### Station Analysis</br>
Several more queries were designed to pull the following info:</br>
-Calculate total number of stations.</br>
-Find the most active stations.</br>
-Retrieve the last 12 months of temperature observation data (tobs) and plotting the results as a histogram.</br>

## Step 2 - Climate App</br>
Using all the queries developed above, we designed a Flask API, using FLASK to create routes.</br>
