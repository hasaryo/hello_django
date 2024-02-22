from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<int:post_id>/', views.post, name='post'),
    path('admin/', admin.site.urls),
    path('post', views.blog1, name='home'),
    path('teste/', views.teste, name='teste')
]