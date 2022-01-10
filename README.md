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
### Purpose


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
As we are only using weather data, it does not necessarily indicates that our business will be successful as Oahu, Hawaii still depends largely on tourists as customers and currently with Covid restriction, the lack of tourist customers will still impact business even if the weather is amazing.

I wasn't sure of the table name in sqlite file so I have used the sqlite cli command to find out (more commands here: https://sqlite.org/cli.html): sqlite3 --> .database --> .tables

#### 8. Making the Call:
The "Proper" Conclusion is indicated below on [Summary](#summary)

## Analysis

>June Temperature Aggregates

![June Temperature Aggregates](resources/junetempdesc.png)

>June Temperature

![June Temperature](resources/junetemp.png)



## Summary


## Appendix

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
