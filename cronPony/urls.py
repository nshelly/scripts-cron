from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'views.manage', name="manage"),
    url(r'^add/$', 'views.add', name="add"),
    url(r'^edit/(?P<job>.*)$', 'views.add', name="edit"),
)
