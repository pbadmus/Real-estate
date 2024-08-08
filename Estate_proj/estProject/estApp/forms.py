from .models import Housing
from django import forms
from django.contrib.auth.models import User

ROLE_CHOICES = [
    ('buyer', 'Buyer'),
    ('seller', 'Seller'),
]

class RegisterUser(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    role = forms.ChoiceField(choices=ROLE_CHOICES, label="Role")
    
    class Meta:
        model = User
        fields = ["username","password", "password_confirm","email", "role"]

        # This is to check if the user enter two matching passwords
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')
            
            # the verfication email can be sent here 
            
            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Passwords do not match!")
            return cleaned_data

class HouseListing(forms.ModelForm):
    class Meta:
        model = Housing
        fields  = '__all__'
        labels = {
            'property_id': "Property ID",
            'title': 'Title',
            'MLS_no': 'Contact Number',
            'exterior_acre': 'Exterior Acre',
            'price': "Price", 
            'location': "Location",
            'status': 'Status',
            'description': "Description"   
        }
        
        widgets = {
            'product_id': forms.NumberInput(attrs={'placeholder':'e.g 1', 'class':'form-control'}), 
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Land or 3-bedroom apartment'}),
            'MLS_no': forms.NumberInput(attrs={'placeholder':'e.g +233***', 'class':'form-control'}),
            'price': forms.NumberInput(attrs={'placeholder':'e.g 10000', 'class':'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the location'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            
        }