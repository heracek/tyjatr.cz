# -*- coding: utf-8 -*-
from django.contrib import admin

from models import ScheduledShow

def activate_scheduled_shows(modeladmin, request, queryset):
    queryset.update(active=True)
activate_scheduled_shows.short_description = u'Aktivuj'

def deactivate_scheduled_shows(modeladmin, request, queryset):
    queryset.update(active=False)
deactivate_scheduled_shows.short_description = u'Deaktivuj'

class ScheduledShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'show', 'time', 'active')
    list_filter = ('date', 'show', 'active')
    actions = [activate_scheduled_shows, deactivate_scheduled_shows]
admin.site.register(ScheduledShow, ScheduledShowAdmin)
