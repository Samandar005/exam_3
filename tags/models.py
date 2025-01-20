from django.db import models
from catalogs.base_model import BaseModel


class Tag(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

