from django.contrib import admin
from .models import Item

class itemAdmin(admin.ModelAdmin):
    list_display = ('item', 'date', 'due')
    list_filter = ['date']


# Register your models here.
admin.site.register(Item, itemAdmin)