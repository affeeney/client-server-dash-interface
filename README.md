# client-server-dash-interface
1.	Summary
This application is a web dashboard to interact with animal rescue center database. Users can explore the mongodb in an easy and streamlined way with visuals and different filters to quickly and accurately query for data and find documents.
Tools – Dash, Plotly, MongoDB
This application follows MVC design pattern. MongoDB serves as the permanent storage and model, while the dashboard serves as the view. The control is the logic behind the interface. 
2.	Features
Query Filtering:
There are buttons integrated into the dashboard that has the functionality to query for results with different parameters. Some include:
-Water Rescue
-Wilderness Rescue
-Individual Tracking
Dynamic Data:
-Displays data directly from the database
-Sorting, filtering, etc
-Automatic tables update
Geolocation Map:
-Displays map and location markers
-Tooltip popup information
Pie Chart:
-Dynamic updated chart
-Represent through visible dataset
3. Tools
-MongoDB: Stores our animal data. Tis was chosen for it’s flexibility with the documents and it’s integration with python.
-Dash: This is the framework for building the interface. Python is an easy to use language and is also integrated with python. Easy way to interact with data.
-Plotly: Minimal code to make and distribute interactive charts.
4. Reproduction
	1. Run your terminal
	2. Direct to AAC
	3. Make sure the 3 files and image are all in the same directory.
	4. Run cell script.
	5. Interface should appear.
5. Challenges
During development, I did encounter issues with the system. Connecting to the database was an issue where the correct parameters were not used in the constructor for the code as well as the port parameter when running the method that executes the application. Integrating the geolocation feature was also crashing the app until I handled the execution correctly and error handling. Image loading error could occur if the image is not the same as the application code.
6. Resources
https://pymongo.readthedocs.io/
https://plotly.com/python/plotly-express/
https://pymongo.readthedocs.io/
