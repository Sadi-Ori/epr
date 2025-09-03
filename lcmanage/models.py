# # godown/models.py
# from django.db import models

# class Consignnee(models.Model):
#     # Foreign Keys will be used for Category and Product Group later,
#     # but for now, we'll use simple CharFields.
#     Type = models.CharField(max_length=100)
#     Consignee_name = models.CharField(max_length=100)
#     Consingnee_owner_name = models.CharField(max_length=255)
#     Contact_number = models.CharField(max_length=15)
#     Consignee_address = models.CharField(max_length=50)
#     Registration_number = models.CharField(max_length=50)

#     def __str__(self):
#         return self.title

# # class Godown(models.Model):
# #     godown_name = models.CharField(max_length=255)
# #     godown_ghat = models.CharField(max_length=255)
# #     address = models.TextField()
# #     contact_number = models.CharField(max_length=15)
# #     TYPE_CHOICES = [
# #         ('self', 'Self'),
# #         ('medium', 'Medium'),
# #     ]
# #     type = models.CharField(max_length=20, choices=TYPE_CHOICES)
# #     sales_hub = models.CharField(max_length=255)

# #     def __str__(self):
# #         return self.godown_name

# # class Dump(models.Model):
# #     # We will relate this to the Godown model later using a ForeignKey,
# #     # but for now, we'll use a simple CharField.
# #     godown_name = models.CharField(max_length=255)
# #     dump_name = models.CharField(max_length=255)
# #     sales_hub = models.CharField(max_length=255)

# #     def __str__(self):
# #         return self.dump_name

# # class CostCenter(models.Model):
# #     entry_date = models.DateField()
# #     cost_center_name = models.CharField(max_length=255)
# #     STATUS_CHOICES = [
# #         ('active', 'Active'),
# #         ('inactive', 'Inactive'),
# #     ]
# #     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')

# #     def __str__(self):
# #         return self.cost_center_name


# lcmanage/models.py
from django.db import models

class Consignee(models.Model):
    CONSIGNEE_TYPES = [
        ('local', 'Local'),
        ('overseas', 'Overseas'),
        ('both', 'Both'),
    ]
    consignee_type = models.CharField(max_length=20, choices=CONSIGNEE_TYPES, default='local')
    consignee_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    reg_number = models.CharField(max_length=50)
    address = models.TextField()

    def __str__(self):
        return self.consignee_name

class LC(models.Model):
    STATUS_CHOICES = [
        ('select_status', 'Select Status'),
        ('running', 'Running'),
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    lc_number = models.CharField(max_length=100, unique=True)
    mv = models.CharField(max_length=255, verbose_name="Mother Vessel")
    allot_lc = models.CharField(max_length=100)
    product = models.CharField(max_length=255)
    consignee = models.CharField(max_length=255)
    bank_info = models.CharField(max_length=255)
    entry_date = models.DateField(auto_now_add=True)
    lc_date = models.DateField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='select_status')
    lc_account = models.CharField(max_length=100, null=True, blank=True)
    lc_bank = models.CharField(max_length=255, null=True, blank=True)
    lc_bank_branch = models.CharField(max_length=255, null=True, blank=True)
    exporter_info = models.CharField(max_length=255, null=True, blank=True)
    registration_no = models.CharField(max_length=100, null=True, blank=True)
    exporter_country = models.CharField(max_length=100, null=True, blank=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lc_open_date = models.DateField(null=True, blank=True)
    sale_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='select_status')

    def __str__(self):
        return self.lc_number