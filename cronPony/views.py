from django.shortcuts import get_object_or_404, render_to_response, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from cronPony.forms import CronjobForm
from django.template import RequestContext
import CronParser

def manage(request):
    context = {}
    # Read in current crontab here
    env_vars, context["jobs"] = CronParser.read()
    context["email"] = env_vars["MAILTO"]
    context["logfile"] = env_vars["LOGFILE"]

    return render_to_response('manage.html', context)

def add(request):
    print "in add view"
    if request.method == 'POST':
        form = CronjobForm(request.POST)
        if form.is_valid():
            # Add code to add cronjob to crontab here
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

            # can add to crontab as such:
            # crontab -l | (cat;echo "00 1 * * * /monitor_file_system") | crontab
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
        

def edit(request, id=0):
    pass

