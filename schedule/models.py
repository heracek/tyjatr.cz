# -*- coding: utf-8 -*-
import datetime
from django.db import models

from shows.models import Show

class ScheduledShow(models.Model):
    show = models.ForeignKey(Show, verbose_name=u'prědstavení')
    date = models.DateField(u'datum', default=datetime.datetime.now)
    time = models.TimeField(u'čas', default=datetime.time(19, 30))
    
    class Meta:
        ordering = ['date', 'time']
        verbose_name = u'Představení na programu'
        verbose_name_plural = u'Představení na pragramu'
    
    def __unicode__(self):
        return u'%s %s - %s' % (self.date, self.time, self.show)
    
