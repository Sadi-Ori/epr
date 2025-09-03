# purchasemanage/forms.py
from django import forms
from .models import Supplier, Purchase

class SupplierForm(forms.ModelForm):
    DISTRICTS = [
        ('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'), ('Barisal', 'Barisal'),
        ('Bhola', 'Bhola'), ('Bogra', 'Bogra'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'),
        ('Chittagong', 'Chittagong'), ('Chuadanga', 'Chuadanga'), ('Comilla', 'Comilla'), ('Cox\'s Bazar', 'Cox\'s Bazar'),
        ('Dhaka', 'Dhaka'), ('Dinajpur', 'Dinajpur'), ('Faridpur', 'Faridpur'), ('Feni', 'Feni'),
        ('Gaibandha', 'Gaibandha'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Habiganj', 'Habiganj'),
        ('Jaipurhat', 'Jaipurhat'), ('Jamalpur', 'Jamalpur'), ('Jessore', 'Jessore'), ('Jhalokati', 'Jhalokati'),
        ('Jhenaidah', 'Jhenaidah'), ('Khagrachhari', 'Khagrachhari'), ('Khulna', 'Khulna'), ('Kishoreganj', 'Kishoreganj'),
        ('Kurigram', 'Kurigram'), ('Kushtia', 'Kushtia'), ('Lakshmipur', 'Lakshmipur'), ('Lalmonirhat', 'Lalmonirhat'),
        ('Madaripur', 'Madaripur'), ('Magura', 'Magura'), ('Manikganj', 'Manikganj'), ('Meherpur', 'Meherpur'),
        ('Moulvibazar', 'Moulvibazar'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Naogaon', 'Naogaon'),
        ('Narail', 'Narail'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Natore', 'Natore'),
        ('Netrokona', 'Netrokona'), ('Nilphamari', 'Nilphamari'), ('Noakhali', 'Noakhali'), ('Pabna', 'Pabna'),
        ('Panchagarh', 'Panchagarh'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Rajbari', 'Rajbari'),
        ('Rajshahi', 'Rajshahi'), ('Rangamati', 'Rangamati'), ('Rangpur', 'Rangpur'), ('Satkhira', 'Satkhira'),
        ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Sirajganj', 'Sirajganj'), ('Sunamganj', 'Sunamganj'),
        ('Sylhet', 'Sylhet'), ('Tangail', 'Tangail'), ('Thakurgaon', 'Thakurgaon'),
    ]
    district = forms.ChoiceField(choices=[('', 'Select District')] + DISTRICTS, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Supplier
        fields = ['name', 'contact', 'address', 'district', 'area']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Title'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Contact'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Address', 'rows': 3}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Area'}),
        }

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ['supplier', 'contact', 'address']
        widgets = {
            'supplier': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Enter Supplier Name'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Contact'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address', 'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['supplier'].queryset = Supplier.objects.all()