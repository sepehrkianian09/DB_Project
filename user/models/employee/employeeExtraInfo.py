import datetime

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from .employee import Employee


class EmployeeWorkingHours(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE, primary_key=True)
    working_day = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(6),
    ])
    start_hour = models.TimeField(default=datetime.time())
    end_hour = models.TimeField(default=datetime.time())

    def clean(self):
        super().clean()
        if self.end_hour <= self.start_hour:
            raise ValidationError(f"start_hour should be smaller than end_hour")

    class Meta:
        unique_together = ['employee_id', 'working_day']
