from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

# Create your views here.
def login(request):
    template = 'accounts/login.html'

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user     = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            messages.success(request, "You are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "Your credentials are not correct")
            return redirect('login')    
    else:
        return render(request,template)    
     

def register(request):
    template = 'accounts/register.html'

    if request.method == "POST":

        # get form values
        first_name = request.POST['first_name']
        last_name  = request.POST['last_name']
        username   = request.POST['username']
        email      = request.POST['email']
        password   = request.POST['password']
        password2  = request.POST['password2']

        # check if password match
        if password == password2:
            # check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "That username is already taken")
                return redirect("register")
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "That email is already been used")
                    return redirect("register")
                else:
                    #  create user
                    user = User.objects.create_user(username=username,email=email,password=password2,first_name=first_name,last_name=last_name)
                    # login after register
                    # auth.login(request, user)
                    # messages.success(request, "You are logged in")
                    # return redirect('index')

                    user.save()
                    messages.success(request, "You are now registerd you can log in now")
                    return redirect('login')
        else:
            messages.error(request, "Passwords do not march")
            return redirect('register')
      
       
    else:
        return render(request,template)

def logout(request):
    
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, "You are Now Logged Out")
        return redirect('index')

def dashboard(request):
    template = 'accounts/dashboard.html'
    return render(request,template)