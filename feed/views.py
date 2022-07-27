from django.shortcuts import render
from .models import Feed
from django.http import HttpResponseRedirect


def index(request):
    food = Feed.objects.all()
    return render(request, 'feed.html', {'food': food})


def create(request):
    if request.method == 'POST':
        food = Feed()
        food.price = request.POST.get('price')
        food.producer = request.POST.get('producer')
        food.weight_feed = request.POST.get('weight_feed')
        food.save()
    return HttpResponseRedirect('feed/')