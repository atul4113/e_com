from django.shortcuts import render

# Create your views here.

def index(request):

    context = {"username_is": "Name"}
    template = "index.html"
    return render(request, template, context)
