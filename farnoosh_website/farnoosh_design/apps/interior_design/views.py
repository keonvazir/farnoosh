from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, "interior_design/index.html")

def about(request):
    return render(request, "interior_design/about.html")

def contact(request):
    return render(request, "interior_design/contact.html")

def projects(request):
    return render(request, "interior_design/projects.html")
    


