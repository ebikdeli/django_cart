from django import forms
from django.contrib.auth.models import User, Group, Permission


class UserModelForm(forms.ModelForm):

    class Meta:
        model = User
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
