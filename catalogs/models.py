from catalogs.base_model import BaseModel
from django.db import models


class Catalog(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name}"
