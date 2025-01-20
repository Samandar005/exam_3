from . import views
from django.urls import path


app_name = 'posts'

urlpatterns = [
    path('detail/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.blog_detail, name='detail'),
    path('', views.post_list, name='list')
]
