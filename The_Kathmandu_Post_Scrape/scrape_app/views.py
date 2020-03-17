from django.shortcuts import render
import os, sys
from subprocess import run, PIPE
from .models import TheKathmanduPostScrapeModel

# Create your views here.
def scrape(request):
    context={
        'items': TheKathmanduPostScrapeModel.objects.all(),
        
    }
    return render(request, "homepage.html", context)

