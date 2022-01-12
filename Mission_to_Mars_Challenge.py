#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


# In[3]:


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# In[4]:


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# In[5]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[6]:


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# In[7]:


slide_elem.find('div', class_='content_title')


# In[8]:


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# In[9]:


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images

# In[10]:


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# In[11]:


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# In[12]:


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# In[13]:


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# In[14]:


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


# ### Galaxy Facts Mars

# In[15]:


#The Pandas function read_html() specifically searches for and returns a list of tables found in the HTML. 
#By specifying an index of 0, we're telling Pandas to pull only the first table it encounters, or the first item in 
#the list. Then, it turns the table into a DataFrame.
df = pd.read_html('https://galaxyfacts-mars.com')[0]

#Here, we assign columns to the new DataFrame for additional clarity.
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# In[16]:


df.to_html()


# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

# In[17]:


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)

# <div id="product-section" data-section="product" class="result-list">
browser.is_element_present_by_css('div.result-list', wait_time=1)


# In[18]:


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

html = browser.html
new_soup = soup(html, 'html.parser')
slide_elem = new_soup.select('div.item')


# In[19]:


#<div class="collapsible results">
#d_url = slide_elem.select('div', class_='content_title').get_text()
#news_title

urlpath = []

for each in slide_elem:
    #print(each)
    d_url = each.find('a').get('href')
    print(d_url)
    urlpath.append(d_url)


# In[20]:


for each in urlpath:
    hemisphere = {}
    each_url = f'{url}{each}'
    browser.visit(each_url)
    browser.is_element_present_by_css('h2', wait_time=1)
    html = browser.html
    #each_soup = soup(html, 'html.parser')
    each_soup = soup(html, 'lxml')
    slide_elem = each_soup.select('div.container')[0]

    #browser.links.find_by_partial_text('Sample').click()
    #browser.back()

    img_url = slide_elem.select('a')[1].get('href')
    hemisphere['img_url'] = f'{url}{img_url}'
    hemisphere['title'] = slide_elem.find('h2').get_text()
    hemisphere_image_urls.append(hemisphere)


# In[21]:


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# In[22]:


# 5. Quit the browser
browser.quit()

