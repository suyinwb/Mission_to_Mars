# Mission to Mars

## Background

Robin, who loves astronomy and wants to work for NASA one day, has decided to use a specific method of gathering the latest data: web scraping. Using this technique, she has the ability to pull data from multiple websites, store it in a database, then present the collected data in a central location: a webpage.

Robin wants to be kept up to date with different Mars news, and she's enjoyed the articles published on the NASA news website (Links to an external site.). For her project specifically she would like to extract the most recently published article's title and summary.

Robin knows that she will want to pull the top article and summary sentence.

Robin has carefully staked out the websites she wants to routinely scrape data from. It's her dream to eventually work for NASA, so that's part of why she's chosen two similar sites as sources. Another reason is that these sites have very friendly Terms of Service (or ToS, also known as Terms of Use) when it comes to web scraping.

## Overview of Project
### Purpose

W. Avy likes my analysis, but he wants more information about temperature trends before opening the surf shop. Specifically, he wants temperature data for the months of June and December in Oahu, in order to determine if the surf and ice cream shop business is sustainable year-round.

## Analysis And Challenges

## Methodology: Analytics Paradigm

#### 1. Decomposing the Ask


#### 2. Identify the Datasource
*

#### 3. Define Strategy & Metrics
**Resource:** Python 3, Flask, Pandas, Jupyter Notebook, Splinter, Beautiful Soup, PyMongo, MongoDB, HTML5Lib, LXML

#### 4. Data Retrieval Plan
Using Python SQL toolkit and Object Relational Mapper, sqlAchemy to query and retrieve the data for June & December.

#### 5. Assemble & Clean the Data
While some June & December data has NaN values, there is no difference in the final data analysis if we dropna() or not as the charts will show the same results regardless.

#### 6. Analyse for Trends

Understanding precipitation:

* Light rain — when the precipitation rate is < 2.5 mm (0.098 in) per hour.
* Moderate rain — when the precipitation rate is between 2.5 mm (0.098 in) – 7.6 mm (0.30 in) or 10 mm (0.39 in) per hour.
* Heavy rain — when the precipitation rate is > 7.6 mm (0.30 in) per hour or between 10 mm (0.39 in) and 50 mm (2.0 in) per hour

#### 7. Acknowledging Limitations
As we are only using weather data, it does not necessarily indicates that our business will be successful as Oahu, Hawaii still depends largely on tourists as customers and currently with Covid restriction, the lack of tourist customers will still impact business even if the weather is amazing.

I wasn't sure of the table name in sqlite file so I have used the sqlite cli command to find out (more commands here: https://sqlite.org/cli.html): sqlite3 --> .database --> .tables

#### 8. Making the Call:
The "Proper" Conclusion is indicated below on [Summary](#summary)

## Analysis

2 additional queries were added to get the precipitation for June and December. See the queries below.

```
june_prcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==6).all()
.
.
.
decprcp = session.query(Measurement.date, Measurement.prcp).filter(extract('month', Measurement.date)==12).all()
```

>June Temperature Aggregates

![June Temperature Aggregates](resources/junetempdesc.png)

>June Temperature

![June Temperature](resources/junetemp.png)

As seen above for June between 2010 to 2017, the temperature has a _**average of 74.9 Fahrenheit**_ with  min of 64 Fahrenheit and max of 85 Fahrenheit. From the histogram, the temperature is frequently between 72 to 79 Fahrenheit.

>June Precipitation Aggregates

![June Precipitation Aggregates](resources/juneprcpdesc.png)

>June Precipitation

![June Precipitation](resources/juneprcp.png)

As seen above for June between 2010 to 2017, the precipitation has a _**average of 0.13 mm**_ with  min of 0 mm and max of 4.43 mm. From the histogram, the rain precipitation rarely goes above 2 mm.

>December Temperature Aggregates

![December Temperature Aggregates](resources/dectempdesc.png)

>December Temperature

![December Temperature](resources/dectemp.png)

As seen above for December between 2010 to 2017, the temperature has a _**average of 71.04 Fahrenheit**_ with  min of 56 Fahrenheit and max of 83 Fahrenheit. From the histogram, the temperature is frequently between 66 to 75 Fahrenheit.

>December Precipitation Aggregates

![December Precipitation Aggregates](resources/decprcpdesc.png)

>December Precipitation

![December Precipitation](resources/decprcp.png)

As seen above for December between 2010 to 2017, the precipitation has a _**average of 0.21 mm**_ with  min of 0 mm and max of 6.42 mm. From the histogram, the rain precipitation rarely goes above 2.5 mm.


## Summary


## Appendix
