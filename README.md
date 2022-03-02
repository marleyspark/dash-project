# Graph Application - Graph Application for Dash Project


> Live demo [_here_](https://dash-project-andy.herokuapp.com/).

## Table of Contents

- [General Info](#general-information)
- [Wireframes & User Stories](#wireframe&user-stories)
- [Planning](#planning)
- [Lessons](#lessons)
- [Technologies Used](#technologies-used)
- [Project Status](#project-status)
- [Contact](#contact)

## General Information

The administration of a well known retail store is interested in using data collected over time from their various branches to understand consumer behaviour in the different regions of the country. Our plan is to create interactive visualisations for them generated from their data which tells a story about their customers.

They’ve provided 10 years worth of data collected from all available branches. The data is inconsistent in terms of format and content as the data collection and storage strategy is decided by the manager of a store branch.
What the customer expects is a dashboard that allows them to:

- Track the most purchased and least purchased products & product categories
overall, per region and per city (limit to top 5 and least 5)

- Track the best performing branches overall per region and per city (performance is
measured in both item quantity sold and monetary value of sales made, limit to best
10 and worst 10)

- Per hour sales for the top 10 branches identified

- Identify the top 10 and bottom 10 profitable branches and indicate how profitable they
are. (Calculate profitability by subtracting expense from total sales)

## Wireframes & User Stories

link to [Wireframes and user stories](https://miro.com/app/board/uXjVOJDvhVE=/?invite_link_id=989677105909)

## Planning

To start I created my wireframes and the user stories so I knew what I was aiming for on design. I had hoped to be able to incorporate some bootstrap to this project so it would look more modern but I was unable to in the time frame. 

I had some issues with the data cleanse part of this project which impacted how I had to implement the graphs within this project. 

As I am using a smaller dataset on this application I have made the function take the data transformation load instead of having the data create prior the applications creation. 
This could help with it being a more universal application with only data-dump require and then the functions run the transformation work. 

I created the html visualisation as I worked so this has changed slightly from the original design with the Top and Bottom results being in their own tables so you could see different locations at the same time. 

## Lessons
If I was doing this again I would have the data being fed from a database such as PostgreSQL or SQL, this would help with function transformation. 

I would have liked to spend more time on the look of the graphs data with colour changes and headers. 

I would have liked to make the application look modern and less simple. I would have also added more information to the tables themselves. 
The site is also not mobile friendly which I think is always a must on any website as most people view on mobile or a smaller screen. 

## Technologies Used

- VS-Code
- Github
-Heroku
- Python 3.9.
    Pandas
    Dash
    petl
    virtual environment
    ipynb Notebooks


## Project Status

Project is: _incomplete_
Based on specifications from the customer.


## Contact

Created by Andrew Ralph-Gledhill
