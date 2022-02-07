from django.core.validators import
from django.db import models
from user.models.Employee import Manager


class TypeConversionTransaction(models.Model):

    manager_id = models.ForeignKey(Manager, on_delete=models.CASCADE())
