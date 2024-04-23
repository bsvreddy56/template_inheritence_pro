from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'home.html')


def Contact_View(request):
    return render(request,'Contact.html')


def services_view(request):
    return render(request,'services.html')


def GAlary_view(request):
    return render(request,'galary.html')