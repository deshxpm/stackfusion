from django.contrib import admin
from .models import SampleDetail

class SampleDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'dob', 'email', 'phone', 'added_date', 'active')

admin.site.register(SampleDetail, SampleDetailAdmin)    
