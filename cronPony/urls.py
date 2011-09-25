from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'views.manage', name="manage"),
    url(r'^add/(?P<path>.*)$', 'views.add', name="add"),
    url(r'^edit/(?P<path>.*)$', 'views.add', name="edit"),
)
