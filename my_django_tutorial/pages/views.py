from webbrowser import get
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *arg, **kwarg):
    print(request)
    print(*arg, **kwarg, sep=" ")
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'home.html', {})

def contact_view(request, *arg, **kward):
    return render(request, "contact.html", {})

def about_view(request, *arg, **kwarg):
    return render(request, 'about.html', {})

def social_view(*arg, **kward):
    return HttpResponse("<h1>Social</h1>")