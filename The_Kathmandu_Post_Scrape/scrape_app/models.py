from django.db import models

# Create your models here.
class TheKathmanduPostScrapeModel(models.Model):
    title = models.TextField(max_length= 1500)
    date = models.CharField(max_length= 50)
    link = models.URLField(max_length = 15000)
    description = models.TextField(max_length=15000)
    thumbnail = models.URLField(max_length = 15000)
    crawled_time = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.title
