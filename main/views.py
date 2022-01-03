from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Point


def index(request):
    ad = Point.objects.all()
    context = {'ad': ad}
    return render(request, 'home/home.html', context)


class PointView(CreateView):
    model = Point
    fields = ['title', 'address', 'price', 'image', 'descriptions']
    template_name = 'home/createpoint.html'
    success_url = '/home'




