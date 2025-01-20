from django.contrib import admin
from .models import Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'bod')
    search_fields = ('full_name', 'email')
    list_filter = ('bod',)