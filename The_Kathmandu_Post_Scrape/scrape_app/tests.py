from django.test import TestCase
import datetime
import sys
# Create your tests here.

date_time = datetime.datetime.now()

print("date is ",(sys.argv[1], date_time))