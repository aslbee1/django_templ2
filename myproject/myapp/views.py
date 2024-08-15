from django.shortcuts import render

def index(elen):
    return render (elen,"index.html")

def about(elen):
    return render (elen,"about.html")

def blog(elen):
    return render (elen,"blog.html")

def clas(elen):
    return render (elen,"class.html")


def hello_view(request):
      return render (request,'index.html')

def hello_view(request):
    menu_items = [
        {"name": "Home", "url": "index", "active": True},
        {"name": "About", "url": "about", "active": False},
        {"name": "Classes", "url": "classes", "active": False},
        {"name": "Blog", "url": "blog", "active": False},
    ]
    return render(request, 'index.html', {'menu_items': menu_items})