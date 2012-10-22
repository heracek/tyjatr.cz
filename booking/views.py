# -*- coding: utf-8 -*-
from django.contrib import messages
from django.core.mail import send_mail
from django.db.models import Sum
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView

from schedule.models import ScheduledShow

from forms import BookTicketsForm
from models import Booking

BOOKING_ADMIN_EMAIL = 'lucijeval@seznam.cz'

BOOKING_ADMIN_MAIL = u'''%(show)s
 > Na jméno: %(name)s
 > Pocet vstupenek: %(number_of_tickets)s
From: %(email)s
'''

BOOKING_USER_MAIL = u'''Dobrý den,
vaše rezervace na jméno %(name)s byla úspěšně přijata.

Zarezervovali jste si představení: %(show)s
Počet vstupenek: %(number_of_tickets)s


Vstupenky si, prosím, vyzvedněte nejpozději deset minut před začátkem daného představení. Pokladna otevírá půl hodiny před představením.

Děkujeme Vám a těšíme se na Vás
DS Ty-já-tr
'''



def book_tickets(request):
    if request.method == 'POST':
        form = BookTicketsForm(request.POST)
        if form.is_valid():
            booking = Booking()
            booking.scheduled_show = form.cleaned_data['show']
            booking.name = form.cleaned_data['name']
            booking.email = form.cleaned_data['email']
            booking.number_of_tickets = form.cleaned_data['number_of_tickets']
            
            send_mail(
                subject=u'Rezervace: %s' % booking.scheduled_show,
                message=BOOKING_ADMIN_MAIL % form.cleaned_data,
                from_email='rezervace-neodpovidat@ty-ja-tr.cz',
                recipient_list=[BOOKING_ADMIN_EMAIL],
                fail_silently=False
            )
            
            send_mail(
                subject=u'Rezervace: %s' % booking.scheduled_show,
                message=BOOKING_USER_MAIL % form.cleaned_data,
                from_email='rezervace-neodpovidat@ty-ja-tr.cz',
                recipient_list=[booking.email],
                fail_silently=False
            )
            
            booking.save()
            
            messages.success(request, u'Děkujeme. Potvrzení bylo odesláno na váš email.')
            form = BookTicketsForm()
    else:
        form = BookTicketsForm()
    return render_to_response('booking/base.html', {
        'book_tickets_form': form,
    }, context_instance=RequestContext(request))


class ScheduledShowsBookingOverview(TemplateView):
    template_name = 'booking/sheduled_shows.html'

    def get_context_data(self, **kwargs):
        context = super(ScheduledShowsBookingOverview, self).get_context_data(**kwargs)
        context['scheduled_shows'] = self.scheduled_shows()
        return context

    def scheduled_shows(self):
        return ScheduledShow.objects.annotate(sum_reservations=Sum('booking__number_of_tickets'))

