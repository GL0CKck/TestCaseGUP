from django.urls import path
from .views import index, PointView

app_name = 'main'

urlpatterns = [
    path('home/', index, name='index'),
    path('create/', PointView.as_view(), name='createpoint'),


]