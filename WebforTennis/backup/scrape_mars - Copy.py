# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
import pandas as pd

# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo

def scrape():
    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'html.parser')



    # Examine the results, then determine element that contains sought info
    # results are returned as an iterable list
    news_title = soup.find_all('title')[0].text
    news_p = soup.find_all('p')[0].text


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)


    # URL of page to be scraped
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)


    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    imageurl = soup.find_all('a', class_='fancybox')[0]['data-fancybox-href']
    urlonly = url[:url.find('spaceimages')]
    featured_image_url = urlonly + imageurl 
    featured_image_url


    # URL of page to be scraped
    url = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'html.parser')


    mars_weather = soup.find_all('div', class_='js-tweet-text-container')[0].text
    mars_weather


    # URL of page to be scraped
    url = 'https://space-facts.com/mars/'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'html.parser')


    facts = soup.find('table', id='tablepress-comp-mars')
    factbody = facts.find('tbody')

    #print("facts = ",facts)

    attributes = {}

    for fact in factbody:
        attribute = fact.find('td', class_='column-1').text
        value = fact.find('td', class_='column-2')
        valuetext = value.find('span', class_='mars-s').text
        #print(attribute,valuetext)
        attributes[attribute] = valuetext
        
    attributesDf = pd.DataFrame(list(attributes.items()), columns=['Attribute','Value'])
    attributesDf.reset_index(drop=True, inplace=True)
    #attributesDf.reset_index(inplace=True)
    #attributesDf.drop('index',inplace=True,axis=1)

    factshtml = attributesDf.to_html(index=False)
    factshtml

    # URL of page to be scraped
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'html.parser')

    #print(soup)

    hemisphere_image_urls = []

    images = soup.find_all('div', class_='item')
    print(type(images))

    for imageitems in images:
        #print('iteratons')
        #print(imageitems)
        #imagesitem = image.find('div', class_='item')
        imagedict = {}
        imagedict['title'] = imageitems.find('a').text
        imagedict['img_url'] = url[:url.find('search')-1] + imageitems.find('a').find('img')['src']
        hemisphere_image_urls.append(imagedict)

    print(hemisphere_image_urls)
    

    marsdict = {}

    marsdict['news_title'] = news_title
    marsdict['news_p'] = news_p
    marsdict['featured_image_url'] = featured_image_url
    marsdict['mars_weather'] = mars_weather
    marsdict['factshtml'] = factshtml
    marsdict['hemisphere_image_urls'] = hemisphere_image_urls

    return marsdict
    #print(imagesurl)


