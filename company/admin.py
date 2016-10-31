from django.contrib import admin
from .models import Company
# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name','ruc','createdAt')
	list_filter = ['createdAt']
	search_fields = ['name','ruc']

admin.site.register(Company,CompanyAdmin)
