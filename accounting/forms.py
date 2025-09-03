# accounting/forms.py
from django import forms
from .models import Account

class AccountForm(forms.ModelForm):
    DISTRICTS = [
        ('', 'Select District'), ('Bagerhat', 'Bagerhat'), ('Bandarban', 'Bandarban'), ('Barguna', 'Barguna'), ('Barisal', 'Barisal'),
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

    district = forms.ChoiceField(choices=DISTRICTS, required=False, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = ['ex_type', 'account_id', 'account_title', 'contact_number', 'district', 'area', 'account_status']
        widgets = {
            'ex_type': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Ex Type'}),
            'account_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account ID'}),
            'account_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Account Title'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Contact Number'}),
            'area': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Select Area'}),
            'account_status': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select Status'}),
        }