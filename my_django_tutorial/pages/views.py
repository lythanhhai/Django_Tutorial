from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage_view(request, *arg, **kwarg):
    print(request)
    print(*arg, **kwarg, sep=" ")
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'home.html', {'hello': 'hello world'})

def contact_view(request, *arg, **kward):
    return render(request, "contact.html", {})

def about_view(request, *arg, **kwarg):
    my_context = {
        'my_text': "this is a text",
        'my_number': 23,
        'my_list': [1, 2, 3, 4, 5]
    }
    return render(request, 'about.html', my_context)

def social_view(*arg, **kward):
    return HttpResponse("<h1>Social</h1>")