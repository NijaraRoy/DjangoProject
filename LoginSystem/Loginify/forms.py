from django import forms
from .models import UserDetails

class SignupForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    confirm_password = forms.CharField(widget=forms.PasswordInput, min_length=6)
    
    class Meta:
        model = UserDetails
        fields = ["username", "email", "password"]
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if UserDetails.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)