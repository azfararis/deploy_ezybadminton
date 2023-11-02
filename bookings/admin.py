from django.contrib import admin
from .models import User, Court, Booking

# Register your models here

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'address', 'phoneNo')

@admin.register(Court)
class CourtAdmin(admin.ModelAdmin):
    list_display = ('courtId', 'description', 'price_per_hour')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('userId', 'courtId', 'date', 'time', 'hours', 'totalPrice')
