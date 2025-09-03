# accounting/models.py
from django.db import models

class Account(models.Model):
    EX_TYPE_CHOICES = [
        ('Accounts Payable Vendor', 'Accounts Payable Vendor'),
        ('Account Receivable', 'Account Receivable'),
        ('Administrative Expenses', 'Administrative Expenses'),
        ('Administrative Income', 'Administrative Income'),
        ('Advance Against Expense', 'Advance Against Expense'),
        ('Advance Against Salary', 'Advance Against Salary'),
        ('Advance Deposit and Prepayments', 'Advance Deposit and Prepayments'),
        ('Advance To Employee', 'Advance To Employee'),
        ('Advance To Personnel', 'Advance To Personnel'),
        ('Bank Expenses', 'Bank Expenses'),
        ('Bank Overdraft', 'Bank Overdraft'),
        ('B A D C', 'B A D C'),
        ('Cash and Cash Equivalents', 'Cash and Cash Equivalents'),
        ('Cash In Hand', 'Cash In Hand'),
        ('Depriciation and Amortization', 'Depriciation and Amortization'),
        ('Director Loan', 'Director Loan'),
        ('Direct Expense', 'Direct Expense'),
        ('Direct Overhead', 'Direct Overhead'),
        ('Direct Purchase', 'Direct Purchase'),
        ('Drawings', 'Drawings'),
        ('Factory Building', 'Factory Building'),
        ('Financial Expenses', 'Financial Expenses'),
        ('Furniture and Fixture', 'Furniture and Fixture'),
        ('F D Group', 'F D Group'),
        ('Import Expense', 'Import Expense'),
        ('Income From Additional Sales', 'Income From Additional Sales'),
        ('Income From Bank', 'Income From Bank'),
        ('Income From Others', 'Income From Others'),
        ('Inter Company Accounts', 'Inter Company Accounts'),
        ('Inter Company Current Accounts', 'Inter Company Current Accounts'),
        ('Investment', 'Investment'),
        ('Lc Margin', 'Lc Margin'),
        ('Lc Purchase', 'Lc Purchase'),
        ('Loan Given To Personel', 'Loan Given To Personel'),
        ('Long Term Unsecured', 'Long Term Unsecured'),
        ('Ltr Loan', 'Ltr Loan'),
        ('L C Margin Account', 'L C Margin Account'),
        ('Merger Equivalents Accounts', 'Merger Equivalents Accounts'),
        ('Motor Vehicle', 'Motor Vehicle'),
        ('Motor Vehicles Sales Office', 'Motor Vehicles Sales Office'),
        ('M T D R', 'M T D R'),
        ('Office Building', 'Office Building'),
        ('Office Eqiupment', 'Office Eqiupment'),
        ('Old Accounts Receivable', 'Old Accounts Receivable'),
        ('Opening Stock', 'Opening Stock'),
        ('Other Advance', 'Other Advance'),
        ('Other Liabilities', 'Other Liabilities'),
        ('Other Non-current Assets', 'Other Non-current Assets'),
        ('Paid Up Capital', 'Paid Up Capital'),
        ('Payable Load Bill', 'Payable Load Bill'),
        ('Payable Unload Bill', 'Payable Unload Bill'),
        ('Petty Cash', 'Petty Cash'),
        ('Plant And Equipments', 'Plant And Equipments'),
        ('Property Land And Building', 'Property Land And Building'),
        ('Provision For Expense', 'Provision For Expense'),
        ('Purchase', 'Purchase'),
        ('Renovation And Subscription', 'Renovation And Subscription'),
        ('Reserve Fund', 'Reserve Fund'),
        ('Retained Earnings', 'Retained Earnings'),
        ('Selling And Marketing Expense', 'Selling And Marketing Expense'),
        ('Sales', 'Sales'),
        ('Sales Return', 'Sales Return'),
        ('Security Deposit', 'Security Deposit'),
        ('Share Holders Loan', 'Share Holders Loan'),
        ('Share Money Deposit', 'Share Money Deposit'),
        ('Spare Parts', 'Spare Parts'),
        ('Sub-station And Electric Installation', 'Sub-station And Electric Installation'),
        ('Sundry Creditors', 'Sundry Creditors'),
        ('Trade In Transit', 'Trade In Transit'),
        ('Trade Receivable', 'Trade Receivable'),
        ('Truck and Loary', 'Truck and Loary'),
    ]

    STATUS_CHOICES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]

    ex_type = models.CharField(max_length=100, choices=EX_TYPE_CHOICES, verbose_name="Ex Type")
    account_id = models.CharField(max_length=50, unique=True, verbose_name="Account ID")
    account_title = models.CharField(max_length=255, verbose_name="Account Title")
    contact_number = models.CharField(max_length=15, blank=True, null=True, verbose_name="Contact Number")
    district = models.CharField(max_length=100, blank=True, null=True)
    area = models.CharField(max_length=255, blank=True, null=True)
    account_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active', verbose_name="Account Status")
    
    # Placeholder for Acc Type and Sub Type, as these were not detailed
    acc_type = models.CharField(max_length=100, blank=True, null=True, default='General')
    sub_type = models.CharField(max_length=100, blank=True, null=True, default='N/A')

    def __str__(self):
        return f"{self.account_id} - {self.account_title}"