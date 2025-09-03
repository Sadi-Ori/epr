# godownsystem/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manages.urls')),
    path('lc-manage/', include('lcmanage.urls')),
    path('purchase-manage/', include('purchasemanage.urls')),
    path('journal-manage/', include('journalmanage.urls')),
    path('accounting/', include('accounting.urls')),
]