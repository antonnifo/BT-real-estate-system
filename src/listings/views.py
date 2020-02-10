from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Listing
from .choices import bedroom_choices, price_choices, county_choices 

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
  
    queryset_list = Listing.objects.order_by('-list_date')
    # keywords
    if "keywords" in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

     # city
    if "city" in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)

      # county
    if "county" in request.GET:
        county = request.GET['county']
        if county:
            queryset_list = queryset_list.filter(county__iexact=county) 

      # bedrooms
    if "bedrooms" in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)

     # price
    if "price" in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)                                   


    template = 'listings/search.html'
    context = {
         "counties": county_choices,
         "pricies" : price_choices,
         "bedrooms": bedroom_choices,
         "listings": queryset_list,
         "values"  : request.GET

    }


    return render(request, template, context)
   
