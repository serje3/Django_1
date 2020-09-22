from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password']
        labels = {'username':'','password':''}
        widgets = {'username' : forms.TextInput(attrs={'class':'form-control','id':'usname'}),
                   'password' : forms.PasswordInput(attrs={'class':'form-control','id':'Password1'})}
class RegisterForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class':'mb-1 form-control'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'mb-1 form-control'})
    )
    class Meta(UserCreationForm.Meta):
        labels = {'username':'Имя пользователя'}
        widgets = {'username' : forms.TextInput(attrs={'class':'mb-1 form-control'})}