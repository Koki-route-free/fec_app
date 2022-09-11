from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import UserDB, SolidDB, TemporaryDB, AssetDB, RoomDB

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'


class ClassCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['room_number'].widget.attrs['class'] = 'form-control'
        self.fields['capacity'].widget.attrs['class'] = 'form-control'
        
    class Meta:
        model = RoomDB
        fields = ("room_number", "capacity")


class AssetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #htmlの表示を変更可能にします
        self.fields['student_number'].widget.attrs['class'] = 'form-control'
        self.fields['room_number'].widget.attrs['class'] = 'form-control'
        self.fields['time'].widget.attrs['class'] = 'form-control'
        self.fields['use_num'].widget.attrs['class'] = 'form-control'
        self.fields['sound'].widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = AssetDB
        fields = ("student_number", "room_number", "time", "use_num", "sound")

