from django.db import models
import uuid

# Create your models here

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    creator_id = models.UUIDField(null=True, blank=True)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
