from django import forms, http, urls
from django.views import generic
from django.contrib.auth import mixins
from . import models, forms


# Create your views here.
class RegisterView(generic.CreateView):

    model = models.User
    form_class = forms.UserCreationForm
    success_url = urls.reverse_lazy('cas_login')