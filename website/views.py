from django.shortcuts import render


# Create your views here.
def index(request):
    print('hello')
    return render(request, 'website/index.html')


def dashboard(request):
    return render(request, 'website/dashboard.html')
