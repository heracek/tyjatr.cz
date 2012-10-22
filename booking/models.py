# -*- coding: utf-8 -*-
import datetime
from django.db import models

from schedule.models import ScheduledShow

class Booking(models.Model):
    scheduled_show = models.ForeignKey(ScheduledShow, verbose_name=u'představení')
    name = models.CharField(u'jméno', max_length=250)
    email = models.EmailField()
    number_of_tickets = models.IntegerField(u'počet lístků')
    time_of_booking = models.DateTimeField(u'čas zarezervování', default=datetime.datetime.now)
    
    class Meta:
        ordering = ['time_of_booking']
        verbose_name = u'rezervace'
        verbose_name_plural = u'rezervace'
    
    def __unicode__(self):
        return u'Rezervace představení "%s" na jméno "%s" a počet lístků: %d' % (
            self.scheduled_show, self.name, self.number_of_tickets
        )
