from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *

# Register your models here.
admin.site.register(Book_type)
admin.site.register(Language)
admin.site.register(Book)
admin.site.register(Student)



@admin.register(Person)
class PersonAdmin(ImportExportModelAdmin):
    list_display = ('Title','Author','Type','Language','Summary','Total_copies','Available_copies')