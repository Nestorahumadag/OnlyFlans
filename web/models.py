import uuid
from django.db import models

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(default=uuid.uuid4, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    