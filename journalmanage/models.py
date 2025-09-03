# journalmanage/models.py
from django.db import models

class Journal(models.Model):
    id = models.AutoField(primary_key=True, default=10000000, editable=False)
    date = models.DateField()
    voucher_number = models.CharField(max_length=50)
    description = models.TextField()
    amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    status = models.CharField(max_length=20, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.id:
            last_journal = Journal.objects.order_by('id').last()
            if last_journal:
                self.id = last_journal.id + 1
            else:
                self.id = 10000001
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Journal ID: {self.id}"

class JournalEntry(models.Model):
    journal = models.ForeignKey(Journal, related_name='entries', on_delete=models.CASCADE)
    trn_id = models.CharField(max_length=50)
    account_debit = models.CharField(max_length=100)
    account_credit = models.CharField(max_length=100)
    lc_number = models.CharField(max_length=100)
    note = models.TextField(blank=True)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)

    def __str__(self):
        return f"Entry for Journal: {self.journal.id}"