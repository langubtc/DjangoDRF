from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "school"

