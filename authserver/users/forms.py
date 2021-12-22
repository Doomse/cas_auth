from django.contrib.auth import forms as auth_forms
from django.core import exceptions
from django.conf import settings
from . import models


class UserCreationForm(auth_forms.UserCreationForm):

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == settings.AUTH_USERNAME:
            raise exceptions.ValidationError("The username %(name)s is invalid", code='invalid', params={'name': settings.AUTH_USERNAME})
        return username


    class Meta(auth_forms.UserCreationForm.Meta):
        model = models.User


class UserChangeForm(auth_forms.UserChangeForm):

    class Meta(auth_forms.UserChangeForm.Meta):
        model = models.User