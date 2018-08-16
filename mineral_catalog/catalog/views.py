from django.shortcuts import render

from .models import Mineral


def index(request):
    minerals = Mineral.objects.all()
    template = 'catalog/index.html'
    context = {'minerals': minerals}
    return render(request, template, context)

def detail(request, mineral_id):
    mineral = Mineral.objects.get(pk=mineral_id)
    template = 'catalog/detail.html'
    context = {'mineral': mineral}
    return render(request, template, context)
