from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
# Create your models here.


class Survey(models.Model):
    code = models.CharField(max_length=6, validators=[MinLengthValidator(6)])
    experience = models.IntegerField(
        default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    form_completion = models.BooleanField(
        verbose_name='Ease of form completion')
    recommendation = models.TextField(max_length=200)

    def __str__(self):
        return self.code