from django.shortcuts import render, get_object_or_404, redirect
from  store.models import Product

def index(request):
    featured_products = Product.objects.order_by('-created').filter(featured=True)
    
    context = {
        'featured_products': featured_products,
    }
 
    return render(request, 'pages/index.html', context)
