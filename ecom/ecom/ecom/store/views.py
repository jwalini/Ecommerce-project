from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def product_details(request, id):
    try:
        product = Product.objects.get(id=id)
    except:
        return HttpResponse('404 : Product Not Found')
    
    return render(request, 'product_detail.html', {'product':product})