# forms.py

#Crontab format
#*     *     *   *    *        command to be executed
#-     -     -   -    -
#|     |     |   |    |
#|     |     |   |    +----- day of week (0 - 6) (Sunday=0)
#|     |     |   +------- month (1 - 12)
#|     |     +--------- day of        month (1 - 31)
#|     +----------- hour (0 - 23)
#+------------- min (0 - 59)

from django import forms
from django.forms.widgets import Select

MINUTE_CHOICES =    [['*','*']] + [(i,i) for i in range(60)]
HOUR_CHOICES =      [['*', '*']] + [(i,i) for i in range(24)]
DAY_WEEK_CHOICES =  [['*', '*']] + [
            (0, 'Sun'),
            (1, 'Mon'),
            (2, 'Tues'),
            (3, 'Wed'),
            (4, 'Thur'),
            (5, 'Fri'),
            (6, 'Sat')]
DAY_MONTH_CHOICES = [['*', '*']] + [(i,i) for i in range(32)]

class CronjobForm(forms.Form):
    command = forms.CharField(max_length=200)
    minute = forms.ChoiceField(choices=MINUTE_CHOICES)
    hour = forms.ChoiceField(choices=HOUR_CHOICES)
    day_of_week = forms.ChoiceField(choices=DAY_WEEK_CHOICES)
    day_of_month = forms.ChoiceField(choices=DAY_MONTH_CHOICES)
    should_log = forms.BooleanField(required=True, label="Log?")
    logfile = forms.CharField(max_length=100)
    should_email = forms.BooleanField(required=True, label="Email?")
    log_email = forms.EmailField()
