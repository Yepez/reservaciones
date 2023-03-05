from django.urls import path 
from . import views

app_name = "bookings"
urlpatterns = [
    path('', views.index, name='index'),
    path('product/', views.product_list, name='product_list'),
    path('product/new', views.product_new, name='product_new'),
]