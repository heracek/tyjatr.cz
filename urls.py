from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

admin.site.index_template = 'admin_index.html'

urlpatterns = patterns('',
    url(r'^rezervace/', include('booking.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {}, 'account-login'),
)
