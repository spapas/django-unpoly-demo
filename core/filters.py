import django_filters
from . import models


class CompanyFilter(django_filters.FilterSet):
    class Meta:
        model = models.Company
        fields = {
            "id": ["exact"],
            "name": ["icontains"],
            "address": ["icontains"],
        }
