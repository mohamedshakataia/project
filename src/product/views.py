from django.shortcuts import render
from .models import jumia ,Category
from django.views.generic import ListView 
from django_filters.views import FilterView
from .filters import ProductFilter 
# Create your views here.

class Product_List(FilterView):
    model = jumia
    filterset_class = ProductFilter




def filter_by_category(request,name_category):
    cv = jumia.objects.filter(category__sweetName=name_category)
    return render(request,'product/jumia_filter.html',{'cv':cv })


def brand(request,manufacture):
    model =jumia
    er = jumia.objects.filter(jumia__manufacture=manufacture)
    return render(request,'product/jumia_filter.html',{'er':er})