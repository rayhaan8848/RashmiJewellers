from django.shortcuts import render
from .models import OfferProduct

# Create your views here.
def Home(request):
    offer=OfferProduct.objects.filter(is_active=True)
    context={
        'offer':offer
    }
    return render(request, 'main/home.html',context)
   

