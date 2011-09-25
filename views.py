from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from cronPony.forms import CronjobForm
from django.template import RequestContext

def manage(request):
    # Read in current crontab here
    cron_list = ['cron1', 'cron2']
    return render_to_response('manage.html',
            { 'cron_list' : cron_list } )

def add(request):
    print "in add view"
    if request.method == 'POST':
        form = CronjobForm(request.POST)
        if form.is_valid():
            # Add code to output to crontab here
            data = request.POST
            minute = data["minute"]
            hour = data["hour"] 
            day_of_month = data["day_of_month"]
            month = data["month"]
            day_of_week = data["day_of_week"]
            command = data["command"]
            print """
Adding to crontab:
%5s %5s %5s %5s %5s %5s""" %  \
                (minute, hour, day_of_month, month, day_of_week, command)
            return redirect(manage)
        else:
            print "form is invalid"
            print form.errors

    else:
        form = CronjobForm()
    
    return render_to_response('add.html', 
        { 'form' : form, },
        context_instance=RequestContext(request)
        )
        

def edit(request):
    pass

