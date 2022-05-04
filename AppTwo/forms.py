from django import forms
from django.core import validators
from django.contrib.auth.models import User

from . import models


def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("Needs to start with Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    bot_catcher = forms.CharField(required=False,
                                  widget=forms.HiddenInput,
                                  validators=[validators.MaxValueValidator(0)])

    # def clean_bot_catcher(self):
    #     bot = self.cleaned_data['bot_catcher']
    #     if len(bot) > 0:
    #         raise forms.ValidationError("GOTCHA BOT")
    #     return bot


class NewUserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserProfileInfo
        fields = ['portfolio_site', 'profile_pic']
