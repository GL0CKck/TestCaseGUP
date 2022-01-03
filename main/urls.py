from django.urls import path
from .views import index, PointView

app_name = 'main'

urlpatterns = [
    path('create/', PointView.as_view(), name='createpoint'),
    path('home/', index, name='index'),

]