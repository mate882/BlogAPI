from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

User = get_user_model()

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')