from django.contrib import admin
from django.urls import path
from home import views as homeViews

app_name = 'home'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeViews.home, name='home'),
]