from django.shortcuts import render
from .models import Chicken
from django.http import HttpResponseRedirect


def index(request):
    chickens = Chicken.objects.all()
    return render(request, 'chicken.html', {'chickens': chickens})


def create(request):
    if request.method == 'POST':
        chickens = Chicken()
        chickens.date = request.POST.get('date')
        chickens.weight = request.POST.get('weight')
        chickens.save()
    return HttpResponseRedirect('chicken/')