from django.shortcuts import render
import os, sys
from subprocess import run, PIPE
from .models import TheKathmanduPostScrapeModel
import datetime
import re
# Create your views here.


def scrape(request):
    context={
        'items': TheKathmanduPostScrapeModel.objects.filter(crawled_time__contains = current_datetime()).distinct("link").all(),
        
    }
    return render(request, "homepage.html", context)

def current_datetime():
    target = str(datetime.datetime.now())
    pattern = "\d\d\d\d-\d\d-\d\d"

    result, *_ = re.findall(pattern, target)
    return result