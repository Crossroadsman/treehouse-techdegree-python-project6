from django.shortcuts import render


def index(request):
    template = 'catalog/index.html'
    return render(request, template)
