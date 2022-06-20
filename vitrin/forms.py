from django import forms
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import get_user_model


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput, help_text='simple password')


class UserModelForm(forms.ModelForm):

    class Meta:
        model = get_user_model()
        # fields = '__all__'
        fields = ['username', 'email', 'password']


class GroupModelForm(forms.ModelForm):

    class Meta:
        model = Group
        fields = '__all__'


class PermissionModelForm(forms.ModelForm):

    class Meta:
        model = Permission
        fields = '__all__'
        # fields = ['name', 'codename']
