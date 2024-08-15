from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from .forms import RegisterUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Housing
from django.contrib.auth.models import User
from django.core.mail import send_mail


confirmation_message = ""

@login_required
def home(request):
    return render(request, 'estApp/home.html')


def register_view(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            role = form.cleaned_data.get('role')
            user = User.objects.create_user(email=email,username=username, password=password)
            login(request, user)
            
            if user is not None: 
                send_mail(
                    "Confirmation email from Real Estate",
                    username + " has officially registered as "+role + " on BlueSpace real estate. Welcome and thank you for choosing to work with us."+"    \t\t Kind Regards, \t Customer Service",
                    "badmuspatrick5@gmail.com",
                    [email],
                    fail_silently=False
                )
                
            return redirect('home')
        
    else:
        form = RegisterUser()
    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    error_message = None 
    if request.method == "POST":  
        username = request.POST.get("username")  
        password = request.POST.get("password")  
        user = authenticate(request, username=username, password=password)  
        if user is not None:  
            login(request, user)  
            next_url = request.POST.get('next') or request.GET.get('next') or reverse('home')  
            return redirect(next_url) 
        else:
            error_message = "Invalid username or password, please enter correct credentials."  
    return render(request, 'accounts/login.html', {'error': error_message})



def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
    else:
        return redirect('home') 


