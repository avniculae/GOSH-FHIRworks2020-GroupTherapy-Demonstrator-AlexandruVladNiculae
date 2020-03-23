from django import forms
from .models import Patients

import django_filters


class UserFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    age = django_filters.NumberFilter()

    class Meta:
        model = Patients
        fields = ['name', 'age']
