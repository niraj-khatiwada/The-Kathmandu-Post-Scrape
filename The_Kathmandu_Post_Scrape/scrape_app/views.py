from django.shortcuts import render
from .models import TheKathmanduPostScrapeModel
from django.contrib import messages
import datetime
import re
# Create your views here.


def scrape(request):
    items_query = TheKathmanduPostScrapeModel.objects.filter(crawled_time__contains = current_datetime()).distinct("link")
    if items_query:
        context={
            'items': items_query
            
        }
    else:
        messages.add_message(request, messages.ERROR, "No data found. You need to crawl first")
        return render(request, "homepage.html")

    return render(request, "homepage.html", context)

def current_datetime():
    target = str(datetime.datetime.now())
    pattern = "\d\d\d\d-\d\d-\d\d"

    result, *_ = re.findall(pattern, target)
    return result