# API Wars 


## The Project
My task was to create a little web application which shows data about the Star Wars universe, store visitor preferences with cookies and handle user login with sessions using 

## Technologies

-JavaScript
-Python


## Tasks
It is advised to create the application in the following steps:

Create a web-server. This should render an HTML file containing a table with all the Planets in the Star Wars universe with these data:
- name
- diameter (in km)
- climate
- terrain
- surface water (in percentage)
- population in formatted way
Make a button in each row (in a new column) if the planet has residents. These buttons should open a modal, populated its data with AJAX, containing the list of residents with more detailed information:
name
- height (in meters)
- mass (in kg)
- skin color
- hair color
- eye color
- birth year
- gender (an icon representation)
Create a simple user login system with the following parts (use session for that):
a registration page accessible from the main page through which visitors can create a user-password pair in the database (you are advised to use salted password hashing),
a login page accessible from the main page where the user can log in,
display username and logout link in the header.

## The Data
Every Star Wars related information can be fetched from https://swapi.dev/'s API. This site provides an endpoint with no authentication needed.
