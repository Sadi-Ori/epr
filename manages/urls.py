# godown/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home view for root ('/')
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_edit, name='product_edit'),
    path('godowns/', views.godown_list, name='godown_list'),
    path('godowns/create/', views.godown_create, name='godown_create'),
    path('godowns/<int:pk>/edit/', views.godown_edit, name='godown_edit'),
    path('dumps/', views.dump_list, name='dump_list'),
    path('dumps/create/', views.dump_create, name='dump_create'),
    path('dumps/<int:pk>/edit/', views.dump_edit, name='dump_edit'),
    path('cost-centers/', views.cost_center_list, name='cost_center_list'),
    path('cost-centers/create/', views.cost_center_create, name='cost_center_create'),
    path('cost-centers/<int:pk>/edit/', views.cost_center_edit, name='cost_center_edit'),
]