# -*- coding: utf-8 -*-
from django.db import models

class Show(models.Model):
    name = models.CharField(u'název', max_length=100)
    
    class Meta:
        ordering = ['name']
        verbose_name = u'Představení'
        verbose_name_plural = u'Představení'
    
    def __unicode__(self):
        return self.name
