from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["user_type", "title","dept","ho_br","mobile", 'first_name', 'last_name', 'username', 'email', 'password1', 'password2']

        widgets ={
            'user_type': forms.Select(attrs={'class':'form-control'}),
            'dept': forms.Select(attrs={'class':'form-control'}),
            'ho_br': forms.Select(attrs={'class':'form-control'}),
        }
