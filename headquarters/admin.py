from django.contrib import admin
from .models import HeadQuarters
# Register your models here.

class HeadQuartersAdmin(admin.ModelAdmin):
        list_display = ('address','phone')
        list_filter = ['createdAt']

admin.site.register(HeadQuarters,HeadQuartersAdmin)
