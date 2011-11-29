from django.contrib import admin

from models import ScheduledShow

class ScheduledShowAdmin(admin.ModelAdmin):
    list_display = ('date', 'show', 'time')
    list_filter = ('date', 'show')
admin.site.register(ScheduledShow, ScheduledShowAdmin)
