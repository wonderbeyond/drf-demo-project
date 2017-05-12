from django_filters.rest_framework import FilterSet

from .models import Company


class CompanyFilter(FilterSet):
    class Meta:
        model = Company
        fields = ('area',)
