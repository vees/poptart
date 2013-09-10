from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^api/new/$', 'poptart.pipeline.views.set_with_secret'),
    (r'^$', 'poptart.pipeline.views.index'),
    (r'^(?P<shortlink>.*)$', 'poptart.pipeline.views.redirect'),
)
