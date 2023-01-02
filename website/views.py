from django.shortcuts import render
from website.models import MyApp


# Create your views here.
def index(request):
    print('hello')
    return render(request, 'website/index.html')


def dashboard(request):
    return render(request, 'website/dashboard.html')
