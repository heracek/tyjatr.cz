# -*- coding: utf-8 -*-
import datetime
from django.db import models

from shows.models import Show

class ScheduledShow(models.Model):
    show = models.ForeignKey(Show, verbose_name=u'prědstavení')
    date = models.DateField(u'datum', default=datetime.datetime.now)
    time = models.TimeField(u'čas', default=datetime.time(19, 30))
    can_be_booked = models.BooleanField(u'rezervace zapnuty', blank=True)
    
    class Meta:
        ordering = ['date', 'time']
        verbose_name = u'představení na programu'
        verbose_name_plural = u'představení na pragramu'
    
    def __unicode__(self):
        return u'%s. %s. %s' % (
            self.date.day, self.date.month, self.show)#, self.time.strftime('%H:%M'))

    def total_number_or_reservations(self):
        return self.booking_set.aggregate(sum=models.Sum('number_of_tickets'))['sum']

