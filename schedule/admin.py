# -*- coding: utf-8 -*-
from django.contrib import admin

from models import ScheduledShow

def activate_can_be_booked_scheduled_shows(modeladmin, request, queryset):
    queryset.update(can_be_booked=True)
activate_can_be_booked_scheduled_shows.short_description = u'Zapni rezervace'

def deactivate_can_be_booked_scheduled_shows(modeladmin, request, queryset):
    queryset.update(can_be_booked=False)
deactivate_can_be_booked_scheduled_shows.short_description = u'Vypni rezervace'

class ScheduledShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'show', 'time', 'can_be_booked')
    list_filter = ('date', 'show', 'can_be_booked')
    actions = [activate_can_be_booked_scheduled_shows, deactivate_can_be_booked_scheduled_shows]
admin.site.register(ScheduledShow, ScheduledShowAdmin)
