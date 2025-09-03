# from django import forms
# from .models import Product, Godown, Dump, CostCenter

# # Form for the Product model
# class ConsignneeForm(forms.ModelForm):
#     class Meta:
#         model = Consigneee
#         fields = ['type_form', 'consignee_name', 'consingnee_owner_name', 'contact_number', 'consignee_address', 'registration_number']
#         widgets = {
#             'Type': forms.TextInput(attrs={'class': 'form-control'}),
#             'Consignee_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'Consingnee_owner_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'Contact_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'Consignee_address': forms.TextInput(attrs={'class': 'form-control'}),
#             'Registration_number': forms.TextInput(attrs={'class': 'form-control'}),

#         }

# # # Form for the Godown model
# # class GodownForm(forms.ModelForm):
# #     class Meta:
# #         model = Godown
# #         fields = ['godown_name', 'godown_ghat', 'address', 'contact_number', 'type', 'sales_hub']
# #         widgets = {
# #             'godown_name': forms.TextInput(attrs={'class': 'form-control'}),
# #             'godown_ghat': forms.TextInput(attrs={'class': 'form-control'}),
# #             'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
# #             'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
# #             'type': forms.Select(attrs={'class': 'form-control'}),
# #             'sales_hub': forms.TextInput(attrs={'class': 'form-control'}),
# #         }

# # # Form for the Dump model
# # class DumpForm(forms.ModelForm):
# #     class Meta:
# #         model = Dump
# #         fields = ['godown_name', 'dump_name', 'sales_hub']
# #         widgets = {
# #             'godown_name': forms.TextInput(attrs={'class': 'form-control'}),
# #             'dump_name': forms.TextInput(attrs={'class': 'form-control'}),
# #             'sales_hub': forms.TextInput(attrs={'class': 'form-control'}),
# #         }

# # # Form for the CostCenter model
# # class CostCenterForm(forms.ModelForm):
# #     class Meta:
# #         model = CostCenter
# #         fields = ['entry_date', 'cost_center_name', 'status']
# #         widgets = {
# #             'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
# #             'cost_center_name': forms.TextInput(attrs={'class': 'form-control'}),
# #             'status': forms.Select(attrs={'class': 'form-control'}),
# #         }


# lcmanage/forms.py
from django import forms
from .models import Consignee, LC

class ConsigneeForm(forms.ModelForm):
    class Meta:
        model = Consignee
        fields = ['consignee_type', 'consignee_name', 'owner_name', 'contact', 'reg_number', 'address']
        widgets = {
            'consignee_type': forms.Select(attrs={'class': 'form-control'}),
            'consignee_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Consignee Name'}),
            'owner_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Consignee Owner Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact'}),
            'reg_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Consignee Reg Number'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Consignee Address'}),
        }

class LCForm(forms.ModelForm):
    class Meta:
        model = LC
        fields = [
            'lc_number', 'mv', 'allot_lc', 'product', 'consignee', 'bank_info', 'lc_date', 'quantity',
            'status', 'lc_account', 'lc_bank', 'lc_bank_branch', 'exporter_info', 'registration_no',
            'exporter_country', 'unit_price', 'total_amount', 'lc_open_date'
        ]
        widgets = {
            'lc_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Number'}),
            'mv': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Mother Vessel'}),
            'allot_lc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Allot LC Number'}),
            'product': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Product Name'}),
            'consignee': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Consignee Name'}),
            'bank_info': forms.TextInput(attrs={'class': 'form-control'}),
            'lc_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Type Quantity'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'lc_account': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Account'}),
            'lc_bank': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select LC Bank'}),
            'lc_bank_branch': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type LC Bank Branch'}),
            'exporter_info': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Exporter Info'}),
            'registration_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Type Registration NO'}),
            'exporter_country': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Exporter Country'}),
            'unit_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Type Unit Price'}),
            'total_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Type Total'}),
            'lc_open_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class LCUpdateForm(forms.ModelForm):
    class Meta:
        model = LC
        fields = ['lc_open_date', 'allot_lc', 'quantity', 'lc_bank_branch', 'sale_status']
        widgets = {
            'lc_open_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'allot_lc': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'lc_bank_branch': forms.TextInput(attrs={'class': 'form-control'}),
            'sale_status': forms.Select(attrs={'class': 'form-control'}),
        }