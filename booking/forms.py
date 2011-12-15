# -*- coding: utf-8 -*-
import datetime
from django import forms

from schedule.models import ScheduledShow

MONTH_NAMES = (
    u'leden',
    u'únor',
    u'březen',
    u'duben',
    u'květen',
    u'červen',
    u'červenec',
    u'srpen',
    u'září',
    u'říjen',
    u'listopad',
    u'prosinec',
)

NUMBER_OF_TICKETS_CHOICES = (
    ('', 'vyberte'),
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
)

class BookTicketsForm(forms.Form):
    show = forms.ModelChoiceField(label=u'Představení', queryset=ScheduledShow.objects.all())
    name = forms.CharField(label=u'Vaše jméno')
    email = forms.EmailField(label=u'Váš e-mail')
    number_of_tickets = forms.ChoiceField(label=u'Počet vstupenek', choices=NUMBER_OF_TICKETS_CHOICES)
    
    def __init__(self, *args, **kwargs):
        super(BookTicketsForm, self).__init__(*args, **kwargs)
        self.autoset_show_choices()
    
    def autoset_show_choices(self):
        today = datetime.date.today()
        midnite_today = datetime.datetime(
            year=today.year,
            month=today.month,
            day=today.day,
            hour=23,
            minute=59,
            second=59,
        )
        
        choices = [('', u'vyberte představení')]
        last_month = None
        last_month_shows = []
        
        for show in ScheduledShow.objects.filter(date__gt=midnite_today, can_be_booked=True):
            if last_month != show.date.month:
                last_month = show.date.month
                last_month_shows = []
                choices.append((MONTH_NAMES[show.date.month - 1].upper(), last_month_shows))
            last_month_shows.append((show.pk, unicode(show)))
        
        self.fields['show'].choices = choices
    
