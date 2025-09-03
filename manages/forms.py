# from django import forms
# from .models import Product, Godown, Dump, CostCenter

# # Form for the Product model
# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['category', 'product_group', 'title', 'color', 'unit_type', 'unit_strength', 'open_sale_price', 'allotment_sale_price', 'status']
#         widgets = {
#             'category': forms.TextInput(attrs={'class': 'form-control'}),
#             'product_group': forms.TextInput(attrs={'class': 'form-control'}),
#             'title': forms.TextInput(attrs={'class': 'form-control'}),
#             'color': forms.TextInput(attrs={'class': 'form-control'}),
#             'unit_type': forms.TextInput(attrs={'class': 'form-control'}),
#             'unit_strength': forms.TextInput(attrs={'class': 'form-control'}),
#             'open_sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'allotment_sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }

# # Form for the Godown model
# class GodownForm(forms.ModelForm):
#     class Meta:
#         model = Godown
#         fields = ['godown_name', 'godown_ghat', 'address', 'contact_number', 'type', 'sales_hub']
#         widgets = {
#             'godown_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'godown_ghat': forms.TextInput(attrs={'class': 'form-control'}),
#             'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
#             'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
#             'type': forms.Select(attrs={'class': 'form-control'}),
#             'sales_hub': forms.TextInput(attrs={'class': 'form-control'}),
#         }

# # Form for the Dump model
# class DumpForm(forms.ModelForm):
#     class Meta:
#         model = Dump
#         fields = ['godown_name', 'dump_name', 'sales_hub']
#         widgets = {
#             'godown_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'dump_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'sales_hub': forms.TextInput(attrs={'class': 'form-control'}),
#         }

# # Form for the CostCenter model
# class CostCenterForm(forms.ModelForm):
#     class Meta:
#         model = CostCenter
#         fields = ['entry_date', 'cost_center_name', 'status']
#         widgets = {
#             'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
#             'cost_center_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'status': forms.Select(attrs={'class': 'form-control'}),
#         }

# godown/forms.py
from django import forms
from .models import Product, Godown, Dump, CostCenter

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
            'product_group': forms.TextInput(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_type': forms.TextInput(attrs={'class': 'form-control'}),
            'unit_strength': forms.TextInput(attrs={'class': 'form-control'}),
            'open_sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'allotment_sale_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

class GodownForm(forms.ModelForm):
    class Meta:
        model = Godown
        fields = '__all__'
        widgets = {
            'godown_name': forms.TextInput(attrs={'class': 'form-control'}),
            'godown_ghat': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'sales_hub': forms.TextInput(attrs={'class': 'form-control'}),
        }

class DumpForm(forms.ModelForm):
    class Meta:
        model = Dump
        fields = '__all__'
        widgets = {
            'godown_name': forms.TextInput(attrs={'class': 'form-control'}),
            'dump_name': forms.TextInput(attrs={'class': 'form-control'}),
            'sales_hub': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CostCenterForm(forms.ModelForm):
    class Meta:
        model = CostCenter
        fields = '__all__'
        widgets = {
            'entry_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'cost_center_name': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }