#Run this file to start the scraping process 

import subprocess
import time
import webbrowser

#Django Config
#Migrations
class Django():
       
    def run_server(self):
        run_server = subprocess.run("cd C:/Users/niraj/Documents/Projects/Scraping Kathmandu Post/The_Kathmandu_Post_Scrape && python manage.py runserver", stderr= subprocess.STDOUT, shell= True)
        if run_server.returncode == 0:
            print(f"------Server started------\nReturn Code= {run_server.returncode}")
        else:
            print(f"\n********Error******Run Server*******\n Retur Code: {run_server.returncode}")
        return run_server.returncode
        
#Scrapy related
class Scrapy():

    def crawl_spider(self):
        crawl_spider = subprocess.run("cd C:/Users/niraj/Documents/Projects/Scraping Kathmandu Post/The_Kathmandu_Post_Scrape/kathmandu_post && scrapy crawl the_kathmandu_post",stderr= subprocess.STDOUT, shell= True)
        if crawl_spider.returncode == 0:
            print(f"Crawled---------\nReturn Code= {crawl_spider.returncode}")
        else:
            print(f"\n********Error******Crawl Spider*******\n Return Code: {crawl_spider.returncode}")
        return crawl_spider.returncode

#Django Instance
django  = Django()

#Scrapy Instance
scrapy = Scrapy()
a = scrapy.crawl_spider()
if a == 0:
    webbrowser.open("http://127.0.0.1:8000")
else:
    print("Server was unable to run due to some error during scraping")
#Run server
django.run_server()

