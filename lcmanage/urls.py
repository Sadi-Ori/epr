# lcmanage/urls.py
from django.urls import path
from . import views

app_name = 'lcmanage'

urlpatterns = [
    path('consignees/', views.consignee_list, name='consignee_list'),
    path('consignees/create/', views.consignee_create, name='consignee_create'),
    path('consignees/<int:pk>/edit/', views.consignee_edit, name='consignee_edit'),
    path('lcs/', views.lc_list, name='lc_list'),
    path('lcs/update/<int:pk>/', views.lc_update, name='lc_update'),
]