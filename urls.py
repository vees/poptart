from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
  (r'^$', 'poptart.pipeline.views.index'),
	(r'^(?P<shortlink>[a-zA-Z0-9]{1,4})$', 'poptart.pipeline.views.redirect'),
    # Example:
    # (r'^poptart/', include('poptart.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
