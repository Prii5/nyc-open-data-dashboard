# NYC Senior Services Open Data Dashboard
This project is an interactive data visualization dashboard built using Dash and Plotly, powered by the NYC Open Data portal via the Socrata API. It highlights the accessibility and usage of senior services across New York City boroughs through live public data.

##  Project Overview
The dashboard provides an intuitive interface to explore program distribution, client reach, and service locations. It leverages the Socrata Open Data API to pull real-time .json data from the NYC government portal — with no SDK or tokens — and feeds it directly into a data pipeline built with pandas.

###  Features
- Dropdown filter to select borough of interest
- Visualizations include:
  - Total clients served by program type (bar chart)
  - Count of programs by zip code (bar chart)
  - Program type distribution (pie chart)
  - Client volume per program type (box plot)
  - Program location map (interactive Mapbox)

###  Technologies Used
- Python
- Dash by Plotly
- Pandas
- Plotly Express
- NYC Open Data / Socrata API

### Data Source
- [NYC Open Data - Senior Services Dataset](https://data.cityofnewyork.us/Social-Services/Senior-Center-and-Home-Delivered-Meals/2td3-mfek)

### How It Works
- Pulls .json from the public Socrata API endpoint using pandas.read_json
- Cleans and filters the data in real-time
- Renders interactive visuals with Plotly Express
- Launched through Dash server 

### Try It Live
https://nyc-open-data-dashboard-4.onrender.com

