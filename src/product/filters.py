import django_filters
from .models import jumia

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = jumia
        fields = ['category']