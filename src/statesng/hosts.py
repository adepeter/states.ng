from django.conf import settings
from django.contrib import admin
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'', settings.ROOT_URLCONF, name='statesng_root'),
    host(r'api', 'statesngapps.apis.urls', name='apis'),
    host(r'cpanel', admin.site.urls, name='admin'),
    host(r'pages', 'statesngapps.pages.urls', name='pages'),
)
