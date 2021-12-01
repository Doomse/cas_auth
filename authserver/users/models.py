from django.db import models
from django.contrib.auth import models as auth_models


# Create your models here.
class User(auth_models.AbstractUser):
    """
    Custom user model for extending later
    """

    def save(self, *args, **kwargs) -> None:
        if self._state.adding:
            #TODO preregister user to specified clients
            pass
        return super().save(*args, **kwargs)