import subprocess
import time

#Django Config
#Migrations
class Django():
    def __init__(self):
        pass

    def make_migrations(self):
        try:
            make_migrations = subprocess.run("cd C:/Users/niraj/Documents/Projects/Scraping Kathmandu Post/The_Kathmandu_Post_Scrape && python manage.py makemigrations", stdout= subprocess.PIPE, stderr= subprocess.PIPE, shell= True)
            if make_migrations.returncode==0:
                print(f"------------------------------\n{make_migrations.stdout.decode()}\n------Make Migrations Completed------\nReturn Code= {make_migrations.returncode}")
            else:
                print(f"{make_migrations.stderr.decode()}\n********Error******Make Migrations*******")
        except :
            print(f"{make_migrations.stderr.decode()}***************Exceptions*****Make Migrations**************")   

    def migrate(self):
        try:
            migrate = subprocess.run("cd C:/Users/niraj/Documents/Projects/Scraping Kathmandu Post/The_Kathmandu_Post_Scrape && python manage.py migrate",stderr= subprocess.PIPE, stdout= subprocess.PIPE ,shell = True )
            if migrate.returncode == 0:
                print(f"-------------------------------\n{migrate.stdout.decode()}\n------Make Migrate Completed------\nReturn Code= {migrate.returncode}")
            else:
                print(f"{migrate.stderr.decode()}\n********Error******Make Migrate*******")
        except:
            print(f"{migrate.stderr.decode()}***************Exceptions*****Make Migrate**************")   

    def run_server(self):
        try:
            run_server = subprocess.run("cd C:/Users/niraj/Documents/Projects/Scraping Kathmandu Post/The_Kathmandu_Post_Scrape && python manage.py runserver", stdout= subprocess.PIPE, stderr= subprocess.PIPE, shell= True)
            if run_server.returncode == 0:
                print(f"-------------------------------\n{run_server.stdout.decode()}\n------Server started------\nReturn Code= {run_server.returncode}")
            else:
                print(f"{run_server.stderr.decode()}\n********Error******Run Server*******")
        except:
            print(f"{run_server.stderr.decode()}***************Exceptions*****Run Server**************")   

#Scrapy related
class Scrapy():
    def __init__(self):
        pass

    def crawl_spider(self):

        try:
            crawl_spider = subprocess.run("cd C:/Users/niraj/Documents/Projects/Scraping Kathmandu Post/The_Kathmandu_Post_Scrape/kathmandu_post && scrapy crawl the_kathmandu_post", stderr= subprocess.PIPE, stdout= subprocess.PIPE, shell= True)
            if crawl_spider.returncode == 0:
                print(f"---------------------------------\n{crawl_spider.stdout.decode()}\n----------Crawled---------\nReturn Code= {crawl_spider.returncode}")
            else:
                print(f"{crawl_spider.stderr.decode()}\n********Error******Crawl Spider*******")

        except:
            print(f"{crawl_spider.stderr.decode()}***************Exceptions****Crawl Spider**********")


#Django Instance
Django().make_migrations()
Django().migrate()

#Scrapy Instance
Scrapy().crawl_spider()

#Run server
Django().run_server()
