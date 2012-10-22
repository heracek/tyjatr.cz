from django.conf.urls.defaults import patterns, include, url

from views import BookingsForScheduledShowOverview, ScheduledShowsBookingOverview

urlpatterns = patterns('booking.views',
    url(r'^$', 'book_tickets', name='booking-book-tickets'),
    url(r'^prehled/$', ScheduledShowsBookingOverview.as_view(), name='scheduled-shows-booking-overview'),
    url(r'^prehled/(?P<pk>\d+)/$', BookingsForScheduledShowOverview.as_view(), name='bookings-for-schedules-show-overview'),
)
