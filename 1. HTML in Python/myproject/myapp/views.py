from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def home(request):
    context = {
        'title': 'Django Template Example',
        'message': 'Welcome to Django Template Rendering!',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request, 'index.html', context)
