from django.contrib import admin
from django.urls import path
from menu.views import home, demo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('demo/', demo, name='demo'),
]