from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/pages/index.html')

def project(request):
    return render(request, 'blog/pages/project.html')

def document(request):
    return render(request, 'blog/pages/documents.html')

def contact(request):
    return render(request, 'blog/pages/contact.html')

def films(request):
    return render(request, 'blog/films/films.html')