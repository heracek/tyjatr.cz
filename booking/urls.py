from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('booking.views',
    url(r'^$', 'book_tickets', name='booking-book-tickets'),
)
