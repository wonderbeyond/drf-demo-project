from django.contrib import admin

from .models import Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'alias', 'website', 'area')
    search_fields = ('name', 'alias')
