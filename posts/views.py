from django.shortcuts import render, get_object_or_404, redirect
from tags.models import Tag
from django.db.models import Count
from catalogs.models import Catalog
from .models import Post, Comment
from .forms import CommentForm


def post_list(request):
    posts = Post.objects.annotate(comments_count=Count('comments'))
    selected_catalogs = request.GET.getlist('catalog')
    selected_tags = request.GET.getlist('tag')
    sort_by = request.GET.get('sort', '')
    search_query = request.GET.get('search', '')

    if 'all' in selected_catalogs:
        posts = Post.objects.all()
    elif selected_catalogs:
        posts = posts.filter(catalog__id__in=[int(catalog) for catalog in selected_catalogs if catalog.isdigit()])

    if selected_tags:
        posts = posts.filter(tag__id__in=selected_tags)

    if search_query:
        posts = posts.filter(name__icontains=search_query)

    if sort_by == 'latest':
        posts = posts.order_by('-created_at')
    elif sort_by == 'oldest':
        posts = posts.order_by('created_at')
    elif sort_by == 'popular':
        posts = posts.order_by('-comments_count')

    ctx = {
        'posts': posts,
        'catalogs': Catalog.objects.all(),
        'tags': Tag.objects.all(),
        'selected_catalogs': [int(catalog) for catalog in selected_catalogs if catalog.isdigit()],
        'selected_tags': [int(c) for c in selected_tags],
        'current_sort': sort_by,
        'search_query': search_query,
    }
    return render(request, 'posts/index_with_side_bar.html', ctx)

def blog_detail(request, year, month, day, slug):
    post = get_object_or_404(
        Post,
        slug=slug,
        created_at__year=year,
        created_at__month=month,
        created_at__day=day
    )

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                comment=form.cleaned_data['comment'],
                post=post
            )
            return redirect(post.get_detail_url())
    else:
        form = CommentForm()

    comments = Comment.objects.filter(post=post)

    ctx = {
        'post': post,
        'form': form,
        'comments': comments,
    }

    return render(request, 'posts/post-detail.html', ctx)


