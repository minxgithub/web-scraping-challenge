# Dependencies
from splinter import Browser
from bs4 import BeautifulSoup
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)


# NASA MARS NEWS
def mars_news():
    browser = init_browser()
    news_url = 'https://mars.nasa.gov/news/'
    browser.visit(news_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    result = soup.find_all('div', class_='list_text')[0]
    title = result.find('div', class_="content_title").text
    para = result.find("div", class_="article_teaser_body").text
    date = result.find('div', class_='list_date').text

    return title, para, date

# JPL MARS SPACE IMAGES
def mars_images():
    browser = init_browser()
    image_url = 'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html'
    browser.visit(image_url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    featured_image = soup.find('img', class_='headerimage fade-in')['src']
    featured_image_url = f'https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/{featured_image}'

    return featured_image_url

# MARS FACTS
def mars_facts():
    browser = init_browser()
    mars_facts_url = 'https://space-facts.com/mars/'
    mars_facts_df = pd.read_html(mars_facts_url)[0]
    mars_facts_df.columns=['Description','Mars']
    mars_facts_df.set_index('Description', inplace=True)
    mars_html_table = mars_facts_df.to_html(classes="table table-sm table-striped")

    return mars_html_table

# MARS HEMISPHERES
def mars_hemi():
    browser = init_browser()
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    results = soup.find_all('div', class_='item')

    hemisphere_image_urls = []

    for result in results:
    
        base_url = 'https://astrogeology.usgs.gov'
        redirect = result.a['href']
        link = base_url + redirect
        
        browser.visit(link)
        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')
        
        name = soup.find_all('h2')[0].text
        download = soup.find('div', class_='downloads')
        full_image = download.a['href']
        
        hemisphere_image_urls.append({'title': name, 'img_url': full_image})
    
    return hemisphere_image_urls

# SCRAPED DATA
def scrape():
    browser = init_browser()
    data = {}

    title, para, date = mars_news()
    featured_image_url = mars_images()
    mars_html_table = mars_facts()
    hemisphere_image_urls = mars_hemi()
    data = {
        "news_title" : title,
        "news_p" : para,
        "news_date" : date,
        "featured_image" : featured_image_url,
        "mars_facts" : mars_html_table,
        "hemispheres" :  hemisphere_image_urls
    }
    
    return data