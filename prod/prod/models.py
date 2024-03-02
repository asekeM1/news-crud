from django.db import models

class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.TextField()
    views = models.IntegerField()
    is_active = models.BooleanField()