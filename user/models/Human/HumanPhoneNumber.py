from django.db import models

from user.models.Human import Human


class HumanPhoneNumber(models.Model):
    nationality_code = models.ForeignKey(Human, on_delete=models.CASCADE)
    phone_number = models.AutoField(primary_key=True)


class HumanName(models.Model):
    nationality_code = models.ForeignKey(Human, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20, blank=True)


class HumanAddress(models.Model):
    # todo
    nationality_code = models.ForeignKey(Human, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    fathers_name = models.CharField(max_length=20, blank=True)
