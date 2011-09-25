from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from cronPony.forms import CronjobForm

def manage(request):
    pass

def add(request):
    print "in add view"
    if request.method == 'POST':
        form = CronjobForm(request.GET)
        if form.is_valid():
            # Add code to output to crontab here
            return HttpResponseReirect(manage)
        else:
            # Invalid form
            return render_to_response('add.html', {
                'form' : form 
                })
    else:
        form = CronjobForm()
    
    return render_to_response('add.html', {
        'form' : form,
    })

def edit(request):
    pass

