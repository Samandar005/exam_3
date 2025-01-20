from django.contrib import admin
from .models import Post, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 1

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'author')
    search_fields = ('name', 'author__full_name')
    list_filter = ('author',)
    inlines = [CommentInline]

admin.site.register(Comment)