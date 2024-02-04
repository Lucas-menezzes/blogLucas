from django.shortcuts import render

from datetime import datetime

def index(request):
    return render(request, 'blog/pages/index.html')

def document(request):
    return render(request, 'blog/pages/documents.html')

def contact(request):
    return render(request, 'blog/pages/contact.html')

def films(request):
    return render(request, 'blog/films/films.html')