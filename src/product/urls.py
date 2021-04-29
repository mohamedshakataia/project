from django.urls import path
from . import views



app_name='product'


urlpatterns = [
    path('', views.Product_List.as_view(),name='productname'),
    path('<str:name_category>', views.filter_by_category,name='filter_by_category'),
    path('<str:manufacture>', views.brand,name='brand'),


    

    ]