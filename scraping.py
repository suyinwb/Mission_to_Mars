#dependencies
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt


def scrape_all():
    # Initiate headless driver for deployment
    browser = Browser("chrome", executable_path="chromedriver", headless=True)


    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemispheres": hemispheres(browser)
        }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

    # Scrape Mars News
    # Visit the mars nasa news site
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css("ul.item_list li.slide", wait_time=1)

    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one("ul.item_list li.slide")
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find("div", class_="content_title").get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find("div", class_="article_teaser_body").get_text()

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    #img_url = 'https://spaceimages-mars.com/image/featured/mars3.jpg'

    return img_url
    #return 'https://spaceimages-mars.com/image/featured/mars3.jpg'

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html()

def hemispheres(browser):
    try:
        # 1. Use browser to visit the URL
        url = 'https://marshemispheres.com/'
        browser.visit(url)
        browser.is_element_present_by_css('div.result-list', wait_time=1)

        # 2. Create a list to hold the images and titles.
        hemisphere_image_urls = []

        # 3. Write code to retrieve the image urls and titles for each hemisphere.
        html = browser.html
        new_soup = soup(html, 'html.parser')
        slide_elem = new_soup.select('div.item')

        urlpath = []

        for each in slide_elem:
            #print(each)
            d_url = each.find('a').get('href')
            urlpath.append(d_url)

        for each in urlpath:
            hemisphere = {}
            each_url = f'{url}{each}'
            browser.visit(each_url)
            browser.is_element_present_by_css('h2', wait_time=1)
            html = browser.html
            each_soup = soup(html, 'lxml')
            slide_elem = each_soup.select('div.container')[0]
            img_url = slide_elem.select('a')[1].get('href')
            hemisphere['img_url'] = f'{url}{img_url}'
            hemisphere['title'] = slide_elem.find('h2').get_text()
            hemisphere_image_urls.append(hemisphere)

    except AttributeError:
        return

    return hemisphere_image_urls


if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())
