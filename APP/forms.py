from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def save(self):
        s = super().save(commit=False)
        s.password = make_password(password=self.cleaned_data['password'])
        s.save()
        return s
    
class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30)