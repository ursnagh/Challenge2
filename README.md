# Zyte Coding Assignment - Challenge 2
**Summary:**

This spider will scrape the below fields from http://quotes.toscrape.com/js/ website using Scrapy and Splash.

**Quote**  | **Author Name** | **Tags** | 

**Note:** We are using scrapy + splash since the website we are scraping requires javascript rendering. 



**In order to clone this project use the below command:**

```
git clone https://github.com/ursnagh/Challenge2.git
```

If you like to have an experience of creating your own scrapy spider, execute the steps below in your Terminal: 

**Create a New Scrapy Spider Project**

```
scrapy startproject qoutes
cd quotes
scrapy genspider quotes2scrape quotes.toscrape.com
```

You can overwrite your exisitng *settings.py* and the *./spiders/quotes2scrape.py* file from this repository.

Please ensure you have a docker splash instance running before executing the spider. 

**Use the below command to start a docker splash instance. By default the port used is 8050 which can be modified if  required.**

```
docker run -it -p 8050:8050 scrapinghub/splash
```

To install the pre-requisites given below for the spider run the below commands.

[Scrapy](https://pypi.org/project/Scrapy)

[scrapy_splash](https://pypi.org/project/scrapy-splash/)

```
pip install scrapy

pip install scrapy-splash
```

**Use the below command to export the data into a CSV or JSON format**

```
scrapy crawl quotes2scrape -o quotes2scrape.csv
```

