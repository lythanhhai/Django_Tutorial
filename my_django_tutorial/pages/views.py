from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *arg, **kwarg):
    print(request)
    print(*arg, **kwarg, sep=" ")
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'home.html', {})

def contact_view(*arg, **kward):
    return HttpResponse("<h1>Contact</h1>")

def about_view(*arg, **kwarg):
    return HttpResponse("<h1>About</h1>")

def social_view(*arg, **kward):
    return HttpResponse("<h1>Social</h1>")