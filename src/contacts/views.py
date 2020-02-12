from django.contrib import messages
from django.shortcuts import redirect, render
from  django.core.mail import send_mail
import os

from .models import Contacts

# Create your views here.

def contact(request):

    if request.method == 'POST':
        listing_id    = request.POST['listing_id']
        listing       = request.POST['listing']
        name          = request.POST['name']
        email         = request.POST['email']
        phone         = request.POST['phone']
        message       = request.POST['message']
        user_id       = request.POST['user_id']
        realtor_email = request.POST['realtor_email']


    # check if user has made an enqury

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, "You have already made an enquiry about this listing")
                return redirect('/listings/'+ listing_id)


        contact =Contacts(listing=listing, listing_id=listing_id,name=name, email=email,phone=phone,message=message,
        
           user_id=user_id, realtor_email=realtor_email)

        contact.save()

        # Send mail
        from_email_ = os.getenv('EMAIL_HOST_USER')
        send_mail(
            'Property listing Inquiry',
            f'There has been an inquiry on {listing } login to the admin panel  for more info',
            f'{ from_email_ }',
            [realtor_email],
            fail_silently=False

        )

        messages.success(request, "Your enquiry has been submitted a realtor will get back to you asap")

        return redirect('/listings/'+ listing_id)   

    else:
        return redirect('/listings/'+ listing_id)  
