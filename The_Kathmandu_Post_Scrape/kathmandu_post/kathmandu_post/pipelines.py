# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
import psycopg2
from scrape_app.models import TheKathmanduPostScrapeModel

class KathmanduPostPipeline(object):
    def open_spider(self, spider):
        logging.warning("****Spider is opened ******")
        

    def process_item(self, item, spider):
        logging.warning("*******************Inserting data****************")
        insert = TheKathmanduPostScrapeModel(title = item.get("Title"),date = item.get("Date"), link = item.get("Link"),description = item.get("Description"), thumbnail = item.get("Thumbnail"))
        insert.save()
        return item


    def close_spider(self, spider):
        logging.warning("********Spider Closed*********")
        