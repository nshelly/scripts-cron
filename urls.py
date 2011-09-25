from django.conf.urls.defaults import include, patterns

urlpatterns = patterns('',
    (r'^cron/', include('cronPony.urls')),
)
