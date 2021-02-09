# Web-Scraping-Challenge - Mission to Mars

This homework requires web data scraping and visulization.

Latest news and images, basic facts and astrogeology about mars were scraped from various websites including [NASA](https://mars.nasa.gov/news/), [Jet Propulsion Laboratory](https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html), [Space Facts](https://space-facts.com/mars/), and [USGS Astrogeology](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars).

The scraped data were stored in MongoDB using PyMongo. A function called `scrape` was created to insert and/or update the scraped data in MongoDB. Flask was applied afterwards to create a local serves for rendering a html template (homepage) with all the scraped data for visulization. A button on the homepage would lead to a route called `/scrape` for instant updating and reloading the scraped data in the homepage.


### List of Tools used in this homework 
* Pandas
* BeautifulSoup
* Splinter
* Chromedriver
* Flask-PyMongo
* HTML and Bootstrap