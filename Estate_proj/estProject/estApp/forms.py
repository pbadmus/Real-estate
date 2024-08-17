from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail
from .models import ChangePassword

ROLE_CHOICES = [
    ('buyer', 'Buyer'),
    ('seller', 'Seller'),
]
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class RegisterUser(forms.ModelForm):
    last_name = forms.CharField(max_length=50, label="Last name")
    first_name = forms.CharField(max_length=50, label="First name")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    role = forms.ChoiceField(choices=ROLE_CHOICES, widget=forms.RadioSelect, label="Role")
    
    
    class Meta:
        model = User
        fields = ["email","username","last_name","first_name","password", "password_confirm","role"]

        # This is to check if the user enter two matching passwords
        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')
            email = cleaned_data.get('email')
            
            
            
            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Passwords do not match!")
            return cleaned_data


class ChangePassword(forms.ModelForm):
    old_password = forms.CharField(widget=forms.PasswordInput, label="Old Password")
    new_password = forms.CharField(widget=forms.PasswordInput, label="New Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    
    
    class Meta:
        model = ChangePassword
        fields = ['old_password', 'new_password', 'confirm_password']