# # godown/models.py
# from django.db import models

# class Product(models.Model):
#     # Foreign Keys will be used for Category and Product Group later,
#     # but for now, we'll use simple CharFields.
#     category = models.CharField(max_length=100)
#     product_group = models.CharField(max_length=100)
#     title = models.CharField(max_length=255)
#     color = models.CharField(max_length=50)
#     unit_type = models.CharField(max_length=50)
#     unit_strength = models.CharField(max_length=50)
#     open_sale_price = models.DecimalField(max_digits=10, decimal_places=2)
#     allotment_sale_price = models.DecimalField(max_digits=10, decimal_places=2)
#     STATUS_CHOICES = [
#         ('available', 'Available'),
#         ('unavailable', 'Unavailable'),
#         # Add more choices as needed
#     ]
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

#     def __str__(self):
#         return self.title

# class Godown(models.Model):
#     godown_name = models.CharField(max_length=255)
#     godown_ghat = models.CharField(max_length=255)
#     address = models.TextField()
#     contact_number = models.CharField(max_length=15)
#     TYPE_CHOICES = [
#         ('self', 'Self'),
#         ('medium', 'Medium'),
#     ]
#     type = models.CharField(max_length=20, choices=TYPE_CHOICES)
#     sales_hub = models.CharField(max_length=255)

#     def __str__(self):
#         return self.godown_name

# class Dump(models.Model):
#     # We will relate this to the Godown model later using a ForeignKey,
#     # but for now, we'll use a simple CharField.
#     godown_name = models.CharField(max_length=255)
#     dump_name = models.CharField(max_length=255)
#     sales_hub = models.CharField(max_length=255)

#     def __str__(self):
#         return self.dump_name

# class CostCenter(models.Model):
#     entry_date = models.DateField()
#     cost_center_name = models.CharField(max_length=255)
#     STATUS_CHOICES = [
#         ('active', 'Active'),
#         ('inactive', 'Inactive'),
#     ]
#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

#     def __str__(self):
#         return self.cost_center_name


# godown/models.py
from django.db import models

class Product(models.Model):
    category = models.CharField(max_length=100)
    product_group = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    color = models.CharField(max_length=50)
    unit_type = models.CharField(max_length=50)
    unit_strength = models.CharField(max_length=50)
    open_sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    allotment_sale_price = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS_CHOICES = [
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')

    def __str__(self):
        return self.title

class Godown(models.Model):
    godown_name = models.CharField(max_length=255)
    godown_ghat = models.CharField(max_length=255)
    address = models.TextField()
    contact_number = models.CharField(max_length=15)
    TYPE_CHOICES = [
        ('self', 'Self'),
        ('medium', 'Medium'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    sales_hub = models.CharField(max_length=255)

    def __str__(self):
        return self.godown_name

class Dump(models.Model):
    godown_name = models.CharField(max_length=255)
    dump_name = models.CharField(max_length=255)
    sales_hub = models.CharField(max_length=255)

    def __str__(self):
        return self.dump_name

class CostCenter(models.Model):
    entry_date = models.DateField()
    cost_center_name = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

    def __str__(self):
        return self.cost_center_name