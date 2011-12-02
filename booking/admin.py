from django.contrib import admin

from models import Booking

class BookingAdmin(admin.ModelAdmin):
    list_display = ('scheduled_show', 'name', 'number_of_tickets', 'time_of_booking')
admin.site.register(Booking, BookingAdmin)
