from django.contrib import admin
from .models import Item

class itemAdmin(admin.ModelAdmin):
    list_display = ('item', 'date', 'due', 'complete')
    list_filter = ['date'] 

admin.site.register(Item, itemAdmin)