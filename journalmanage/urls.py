# journalmanage/urls.py
from django.urls import path
from . import views

app_name = 'journalmanage'

urlpatterns = [
    path('list/', views.journal_list, name='journal_list'),
    path('approve/', views.journal_approve, name='journal_approve'),
    path('invoice/<int:pk>/', views.journal_print_invoice, name='journal_print_invoice'),
]