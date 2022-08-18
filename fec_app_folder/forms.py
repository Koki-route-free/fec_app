from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserDB, SolidDB, TemporaryDB, AssetDB

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'