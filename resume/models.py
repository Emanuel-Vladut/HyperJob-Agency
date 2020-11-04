from django.contrib.auth.models import User
from django.db.models import (
    CharField,
    ForeignKey,
    Model,
    CASCADE,
)


# Create your models here.

class Resume(Model):
    description = CharField(max_length=1024)
    author = ForeignKey(User, on_delete=CASCADE)

    # def __str__(self):
    #     return self.description
