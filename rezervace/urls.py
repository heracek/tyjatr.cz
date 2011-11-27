from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('rezervace.views',
    url(r'^$', 'reserve_tickets', name='rezervace-reserve-tickets'),
)
