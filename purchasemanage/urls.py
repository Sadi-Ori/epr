# purchasemanage/urls.py
from django.urls import path
from . import views

app_name = 'purchasemanage'

urlpatterns = [
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/edit/', views.supplier_edit, name='supplier_edit'),
    path('purchases/create/', views.purchase_create_list, name='purchase_create'),
    path('purchases/audit/', views.leaf_purchase_audit, name='leaf_purchase_audit'),
    path('purchases/approve/', views.leaf_purchase_approve, name='leaf_purchase_approve'),
]