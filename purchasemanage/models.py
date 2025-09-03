# purchasemanage/models.py
from django.db import models

class Supplier(models.Model):
    name = models.CharField(max_length=255, verbose_name="Supplier Name")
    contact = models.CharField(max_length=15, verbose_name="Contact")
    address = models.TextField(verbose_name="Address")
    district = models.CharField(max_length=100)
    area = models.CharField(max_length=255)
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return self.name

class Purchase(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('audited', 'Audited'),
        ('approved', 'Approved'),
    ]
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    date = models.DateField(auto_now_add=True)
    purchase_id = models.CharField(max_length=100, unique=True, default='') # Will be generated
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Purchase ID: {self.purchase_id}"

    def save(self, *args, **kwargs):
        if not self.purchase_id:
            # Simple unique ID generation based on timestamp
            import time
            self.purchase_id = f'P-{int(time.time())}'
        super().save(*args, **kwargs)