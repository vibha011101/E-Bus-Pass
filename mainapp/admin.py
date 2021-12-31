from django.contrib import admin
from django.contrib.admin.helpers import Fieldset
from django.db import models
from .models import student,place,bus,payment,goes_to
# Register your models here.
@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display=('usn','sname','saddress','email','branch','sem','photo','password')

@admin.register(place)
class placeAdmin(admin.ModelAdmin):
    list_display=('placeid','pname')


@admin.register(bus)
class busAdmin(admin.ModelAdmin):
    list_display=('busno','placeid','fees')

@admin.register(payment)
class paymentAdmin(admin.ModelAdmin):
    list_display=('reciptno','date_of_pay','busno','usn','validity')

@admin.register(goes_to)
class goes_toAdmin(admin.ModelAdmin):
    list_display=('busno','placeid','boarding_time')

