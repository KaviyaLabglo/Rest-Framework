from django.contrib import admin
from project.models import *
# Register your models here.

class M(admin.ModelAdmin):
    list_display = ('id', )
admin.site.register(Todo,M)
