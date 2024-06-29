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
  - Afterwards, I plot the results of this query on a bar chart.
3. The amount of stations in the station table.
4. The most active station in the measurement table.
  - After which, the lowest, highest, and average temperature for that station are queried from the measurement table.
5. The last 12 months of observation data from the measurement table for the most active station.
  - Using this data, I create a histogram of the temperature observations from the query.

## app.py
...


# Built In
Python.  
Jupyter Notebook.  
SQLite.  


# Resources
Used the following resource to figure out using a color map on a histogram in matplotlib.pyplot.
https://stackoverflow.com/questions/23061657/plot-histogram-with-colors-taken-from-colormap
