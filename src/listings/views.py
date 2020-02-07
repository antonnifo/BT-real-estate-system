from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing

def listings(request):
    template = 'listings/listings.html'

    listings = Listing.objects.order_by('-list_date').filter(is_punlished=True)

    paginator = Paginator(listings,6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context  = {
               'listings':paged_listings,
    }
    return render(request, template,context)

def listing(request, id):

    template = 'listings/listing.html'
    listing  = get_object_or_404(Listing,pk=id)
    context   = {
        "listing": listing
    }

    return render(request, template, context)


def search(request):

    template = 'listings/search.html'
    return render(request, template)
   
