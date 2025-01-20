from django.db import models
from authors.models import Author
from catalogs.base_model import BaseModel
from catalogs.models import Catalog
from tags.models import Tag
from django.utils.text import slugify
from django.urls import reverse


class Post(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, related_name='products')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    description = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    tag = models.ManyToManyField(Tag, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Post, self).save(*args, **kwargs)

    def get_detail_url(self):
        return reverse('posts:detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
        ])


    def __str__(self):
        return f"{self.name}"

class Comment(BaseModel):
    name = models.CharField(max_length=200)
    email = models.EmailField(unique=False)
    comment = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments', null=True)

    def __str__(self):
        return f"{self.name}"