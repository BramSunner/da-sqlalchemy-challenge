# About the Project
A DS project using SQLite, SQLalchemy, and Flask (among other things).

The project consists of two modules:  
1. climate.ipynb
2. app.py

## climate.ipynb
This notebook connects to an sqlite database that contains two tables:

### Measurement
A table containing all climate observation records in Hawaii.  
This table contains five columns:
1. id      : the index of the row.
2. station : the station where the observation was made.
3. date    : the date the observation was made.
4. prcp    : the level of precipitation at the time of observation.
5. tobs    : the temperature at the time of observation. 

### Station
A table containing information about the observation stations in Hawaii.  
This table contains six columns:
1. id        : the index of the row.
2. station   : the station code.
3. name      : the name of the station.
4. latitude  : the latitude of the station.
5. longitude : the longitude of the station.
6. elevation : the elevation of the station.

### Queries
After connecting to the database, a series of queries are made to find out the following:
1. The date of the latest observation in the measurement table.  
2. The last 12 months of observation data in the measurement table.  
Afterwards, I plot the results of this query on a bar chart.

4. The amount of stations in the station table.
5. The most active station in the measurement table.  
After which, the lowest, highest, and average temperature for that station are queried from the measurement table.

7. The last 12 months of observation data from the measurement table for the most active station.  
Using this data, I create a histogram of the temperature observations from the query.

## app.py
This script aims to provide user interaction functionality to the Hawaii sqlite database mentioned above.  

Using Flask in Python, I create a page with 6 endpoints:
1. / ... The home page.  
This page shows a quick greeting and the available endpoints that can be accessed--as well as a note on using some of the endpoints.  

2. /api/v1.0/precipitation  
This page shows the past 12 months of precipitation data to the user.  
First, it grabs the most recent observation and records the date.  
Then, the database is queried for results in a range of 12 months before the date up until the date.  
This information is returned as a JSON.  

3. /api/v1.0/stations  
This page shows the user a list of station codes and station names from the database.  
A single query is made to the station table for the 'station' and 'name' values of all rows.  
This data is returned as a JSON.  

4. /api/v1.0/tobs  
This page shows the user the past 12 months of temperature observations from the most active station in the database.  
First, the database is queried for the most recent observation and that date is saved.  
Second, the database is queried for the most active station and that station's code, name, and number of observations are saved.  
Then, I make a query that grabs every observation logged 12 months prior or up until the saved date that originated from the most active station.  
This data is converted to a JSON and returned to the page.  

6. /api/v1.0/<start_date>  
This page takes a user variable 'start_date'.  
Then, a query is made to the database to grab the minimum temperature, maximum temperature, and average of all temperatures from observations logged on or after the 'start_date'.  
These results are converted into a JSON and shown to the user.  

8. /api/v1.0/<start_date>/<end_date>  
This page takes two user variable 'start_date' and 'end_date'.  
Then, a query is made to the database to grab the minimum temperature, maximum temperature, and average of all temperatures from observations logged on or after the 'start_date' and on or before the 'end_date'.  
These results are converted into a JSON and shown to the user.  

# Built In
Python.  
Jupyter Notebook.  
SQLite.  


# Resources
Used the following resource to figure out using a color map on a histogram in matplotlib.pyplot.
https://stackoverflow.com/questions/23061657/plot-histogram-with-colors-taken-from-colormap
