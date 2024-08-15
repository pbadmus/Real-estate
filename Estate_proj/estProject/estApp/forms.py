from django import forms
from django.contrib.auth.models import User
from django.core.mail import send_mail

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
            email = cleaned_data.get('email')
            
            # the verfication email can be sent here 
            
            if password and password_confirm and password != password_confirm:
                raise forms.ValidationError("Passwords do not match!")
            return cleaned_data
