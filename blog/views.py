from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'blog/index.html')

def project(request):
    return render(request, 'blog/project.html')

def document(request):
    return render(request, 'blog/documents.html')

def contact(request):
    return render(request, 'blog/contact.html')