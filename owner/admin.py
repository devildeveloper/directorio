
from django.contrib import admin
from .models import Owner
# Register your models here.

class OwnerAdmin(admin.ModelAdmin):
        list_display = ('name','email')
        list_filter = ['createdAt']
        search_fields = ['name','email']

admin.site.register(Owner,OwnerAdmin)
