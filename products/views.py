from django.shortcuts import render
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    # if request.user.is_authenticated():
    #     username_is = "Atul Kumar Patel"
    #     context = {"username_is": request.user}
    # else:
    #     context = {"username_is": request.user}
    context = {"username_is": "Atul Kumar Patel"}
    template = "index.html"
    return render(request, template, context)

@csrf_exempt
def all(request):
    products = Product.objects.all()
    context = {'products' : products}
    template = "products/all.html"
    return render(request, template, context)
