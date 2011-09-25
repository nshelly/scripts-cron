from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from cronPony.forms import CronjobForm

def manage(request):
    pass

def add(request):
    if request.method == 'GET':
        form = CronjobForm(request.GET)
        if form.is_valid():
            return HttpResponseReirect(manage)
    else:
        form = CronjobForm()

    return render_to_response('cronPony/add.html', {
        'form' : form,
    })

def edit(request):
    pass

