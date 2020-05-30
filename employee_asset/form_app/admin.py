from django.contrib import admin
from .models import BeaconAsset
from import_export.admin import ImportExportModelAdmin
# Register your models here.



@admin.register(BeaconAsset)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )