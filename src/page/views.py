from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

def index(request):

    template = 'page/index.html'

    listings = Listing.objects.order_by('-list_date').filter(is_punlished=True)[:3]

    context = {
           "listings": listings,
    }
    return render(request, template, context)

def about(request):
    
    template = 'page/about.html'

    realtor = Realtor.objects.order_by('-hire_date')

    mvp     = Realtor.objects.all().filter(is_mvp=True)
    
    context = {
        "realtors" : realtor,
        "mvp"      :mvp,
    }
    return render(request, template, context)
