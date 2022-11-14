from django.contrib import admin
from project.models import *
# Register your models here.






class pro(admin.ModelAdmin):
    list_display = ('id', )
admin.site.register(product,pro)

class b(admin.ModelAdmin):
    list_display = ('id', )
admin.site.register(Brand,b)

from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']