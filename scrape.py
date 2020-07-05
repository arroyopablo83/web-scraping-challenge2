# Dependencies
import requests
import json
import os
from bs4 import BeautifulSoup as bs
import pymongo
from splinter import Browser
import pandas as pd
import re

def scrape():

    url = "https://mars.nasa.gov/news/?page=1&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = bs(response.text, "html.parser")
    soup.find_all("div", class_="content_title")

    results = soup.find_all("div", class_="content_title")

    headlines = []

    for x in results:
        print(x.find("a").text)
        y = x.find("a").text
        headlines.append(y.strip("\n \t"))

    #JPL Mars Space Images

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit("https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars")


    image = browser.find_by_id("full_image")

    image.click()

    image2 = browser.find_by_css(".fancybox-image")[0]

    image2

    
    imageMars = image2["src"]



    #Mar Weather

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit("https://twitter.com/marswxreport?lang=en")

    soup = bs(browser.html, "html.parser")
    tweets = soup.find_all(string=re.compile("InSight"))

    mars_weather  = tweets[0]

   

    #Mars Facts

    url = "https://space-facts.com/mars/"

    tables = pd.read_html(url)[0]

    tableHtml = tables.to_html()

    #Mars Hemispheres

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=False)
    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    #Imagen
    mars1 = browser.find_by_css(".thumb")
    mars1.click()
    mars1 = browser.find_by_css(".downloads")
    mars11 = mars1.find_by_css("a")
    url1 = mars11["href"]
    print(url1)

    #Title
    title1 = browser.find_by_css("h2.title")
    title1 = title1.value
    print(title1)

    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    #Imagen
    mars1 = browser.find_by_css(".thumb")[1]
    mars1.click()
    mars1 = browser.find_by_css(".downloads")
    mars11 = mars1.find_by_css("a")
    url2 = mars11["href"]
    print(url2)

    #Title
    title2 = browser.find_by_css("h2.title")
    title2 = title2.value
    print(title2)

    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    #Imagen
    mars1 = browser.find_by_css(".thumb")[2]
    mars1.click()
    mars1 = browser.find_by_css(".downloads")
    mars11 = mars1.find_by_css("a")
    url3 = mars11["href"]
    print(url3)

    #Titulo
    title3 = browser.find_by_css("h2.title")
    title3 = title3.value
    print(title3)

    browser.visit("https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars")

    #Imagen
    mars1 = browser.find_by_css(".thumb")[3]
    mars1.click()
    mars1 = browser.find_by_css(".downloads")
    mars11 = mars1.find_by_css("a")
    url4 = mars11["href"]
    print(url4)

    #Titulo
    title4 = browser.find_by_css("h2.title")
    title4 = title4.value
    print(title4)

    hemisphere_image_urls = [
            {"title": title1 ,"img_url":url1},
            {"title": title2 ,"img_url":url2},
            {"title": title3 ,"img_url":url3},
            {"title": title4 ,"img_url":url4}
    ]

    return {
        "headlines" : headlines[0],
        "imageMars" : imageMars,
        "mars_weather" : mars_weather,
        "mars_facts" : tableHtml,
        "hemisphere_image_urls" : hemisphere_image_urls
    }



if __name__ == "__main__":
    x = scrape()
    print(x)
