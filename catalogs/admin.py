from django.contrib import admin
from .models import Catalog
from posts.models import Post

class PostInline(admin.StackedInline):
    model = Post
    extra = 1

@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    inlines = [PostInline]