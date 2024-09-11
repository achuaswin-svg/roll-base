# myapp/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

class RegistrationForm(UserCreationForm):
    ROLES = [
        ('user', 'User'),
        ('admin', 'Admin'),
    ]
    role = forms.ChoiceField(choices=ROLES, widget=forms.RadioSelect)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']

class LoginForm(AuthenticationForm):
     def get_user(self):
        username = self.cleaned_data.get('username')
        try:
            user = CustomUser.objects.get(username=username)
            return user
        except CustomUser.DoesNotExist:
            return None