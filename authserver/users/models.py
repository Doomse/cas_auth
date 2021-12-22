from django.db import models
from django.contrib.auth import models as auth_models
import threading
from . import utils


# Create your models here.
class User(auth_models.AbstractUser):
    """
    Custom user model for extending later
    """

    def save(self, *args, **kwargs) -> None:
        if self._state.adding:
            t = threading.Thread(target=utils.register_username, kwargs={'user': self.object})
            t.start()
        return super().save(*args, **kwargs)