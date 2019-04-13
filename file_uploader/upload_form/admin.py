from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import FileNameModel

class FileNameAdmin(admin.ModelAdmin):
    list_display = ('id', 'file_name', 'upload_time')
    list_display_links = ('id', 'file_name')

admin.site.register(FileNameModel, FileNameAdmin)