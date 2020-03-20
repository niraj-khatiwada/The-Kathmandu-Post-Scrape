import subprocess
import time

#Django Config
#Migrations
class Django():
       
    def run_server(self):
        run_server = subprocess.run("cd C:/Users/niraj/Documents/Projects/Scraping Kathmandu Post/The_Kathmandu_Post_Scrape && python manage.py runserver", stderr= subprocess.STDOUT, shell= True)
        if run_server.returncode == 0:
            print(f"------Server started------\nReturn Code= {run_server.returncode}")
        else:
            print(f"\n********Error******Run Server*******\n Retur Code: {run_server.returncode}")
        
#Scrapy related
class Scrapy():

    def crawl_spider(self):
        crawl_spider = subprocess.run("cd C:/Users/niraj/Documents/Projects/Scraping Kathmandu Post/The_Kathmandu_Post_Scrape/kathmandu_post && scrapy crawl the_kathmandu_post",stderr= subprocess.STDOUT, shell= True)
        if crawl_spider.returncode == 0:
            print(f"Crawled---------\nReturn Code= {crawl_spider.returncode}")
        else:
            print(f"\n********Error******Crawl Spider*******\n Return Code: {crawl_spider.returncode}")

#Django Instance
django  = Django()

#Scrapy Instance
scrapy = Scrapy()
scrapy.crawl_spider()
#Run server
django.run_server()
