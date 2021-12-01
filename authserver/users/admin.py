from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from . import models, forms


class UserAdmin(auth_admin.UserAdmin):
    form = forms.UserChangeForm
    add_form = forms.UserCreationForm

# Register your models here.
admin.site.register(models.User, UserAdmin)