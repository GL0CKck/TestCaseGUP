from django.urls import path
from .views import index

app_name = 'main'

urlpatterns = [
    path('home/', index, name='index'),
]