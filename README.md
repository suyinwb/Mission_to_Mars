# Mission to Mars

## Background

Robin, who loves astronomy and wants to work for NASA one day, has decided to use a specific method of gathering the latest data: web scraping. Using this technique, she has the ability to pull data from multiple websites, store it in a database, then present the collected data in a central location: a webpage.

Robin wants to be kept up to date with different Mars news, and she's enjoyed the articles published on the NASA news website (Links to an external site.). For her project specifically she would like to extract the most recently published article's title and summary.

Robin knows that she will want to pull the top article and summary sentence.

Robin has carefully staked out the websites she wants to routinely scrape data from. It's her dream to eventually work for NASA, so that's part of why she's chosen two similar sites as sources. Another reason is that these sites have very friendly Terms of Service (or ToS, also known as Terms of Use) when it comes to web scraping.

Robin has finished her first Mars-related scrape. All of the practice and study is starting to pay off. It's a fantastic first step to creating her web application. The next step is to scrape the featured image from another Mars website. Once the image is scraped, we'll want to add it to our web app as well.

The next bit of information Robin wants to have included in her app is a collection of Mars facts. With news articles and high-quality images, a collection of facts is a solid addition to her web app.

She already has decided which webpage she'll use for fact scraping, but the information is held in a table format.

## Overview of Project

Robin's web app is looking good and functioning well, but she wants to add more polish to it. She had been admiring images of Mars’s hemispheres online and realized that the site is scraping-friendly. She would like to adjust the current web app to include all four of the hemisphere images. To do this, you’ll use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.


### Purpose

Scrape 3 different websites to get Mars / NASA related data.


## Analysis And Challenges

## Methodology: Analytics Paradigm

#### 1. Decomposing the Ask


#### 2. Identify the Datasource
*

#### 3. Define Strategy & Metrics
**Resource:** Python 3, Flask, Pandas, Jupyter Notebook, Splinter, Beautiful Soup, PyMongo, MongoDB, HTML5Lib, LXML

#### 4. Data Retrieval Plan


#### 5. Assemble & Clean the Data

#### 6. Analyse for Trends



#### 7. Acknowledging Limitations
Using Mac OS, define the mongo dbpath when starting mongodb.
```
mongod --dbpath /usr/local/var/mongodb
```
Can also look into defining this path permanently in /etc/ but not sure where it is supposed to be in Mac OS.


#### 8. Making the Call:
The "Proper" Conclusion is indicated below on [Summary](#summary)

## Analysis

>June Temperature Aggregates

![June Temperature Aggregates](resources/junetempdesc.png)

>June Temperature

![June Temperature](resources/junetemp.png)



## Summary


## Appendix

Splinter Help
```
Splinter provides 6 methods to finding elements:
browser.find_by_css('h1')
browser.find_by_xpath('//h1')
browser.find_by_tag('h1')
browser.find_by_name('name')
browser.find_by_text('Hello World!')
browser.find_by_id('firstheader')
browser.find_by_value('query')
```

Mongo Commands

* show which database you're working on
```
> db
practicedb
```

* switch database
```
> use practicedb
switched to db practicedb
```

* see how many databases are stored locally
```
> show dbs
admin   0.000GB
config  0.000GB
local   0.000GB
```
