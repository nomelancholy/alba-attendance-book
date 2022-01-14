from django.contrib import admin
from .models import Member
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin


class MemberAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ('name', 'birthdate', 'phone_number')
    search_fields = ['name', 'birthdate', 'phone_number']


admin.site.register(Member, MemberAdmin)
