from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': '/home/ivp/work/tidypub/static'}),
    (r'^$', 'tidypub.main.views.index'),
    (r'^donate$', 'tidypub.main.views.donate'),
    (r'^terms$', 'tidypub.main.views.terms'),
    (r'^contact$', 'tidypub.main.views.contact'),
    (r'^robots.txt$', 'tidypub.main.views.robots'),
    (r'(?P<id>[A-Za-z]+)$', 'tidypub.main.views.view'),
    # Example:
    # (r'^tinypub/', include('tinypub.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
