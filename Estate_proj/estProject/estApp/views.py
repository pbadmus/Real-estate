from django.shortcuts import get_object_or_404, render, redirect
from .forms import RegisterUser, HouseListing
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import HouseListing
from .models import Housing
from django.contrib.auth.models import User


@login_required
def home_view(request):
    return render(request, 'estApp/home.html')


def register_view(request):
    if request.method == "POST":
        form = RegisterUser(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
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
            next_url = request.POST.get('next') or request.GET.get('next') or 'home'  
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


@login_required
def add_house_listing(request):
    if request.method == "POST":
        form = HouseListing(request.POST)
        if form.is_valid():
            house_listing = form.save()
            house_listing.owner = request.user
            house_listing.save()
            return redirect('home')
    form = HouseListing()
    return redirect(request, 'add_house_listing.html', {'form': form})    


@login_required
def view_house_listing(request):
    house_list = HouseListing.objects.filter(owner=request.user)
    return render(request, 'view_house_listings.html', {'house_listings': house_list})


@login_required
def update_house_listing(request, property_id):
    house_list = get_object_or_404(HouseListing, property_id=property_id, owner=request.user)
    if request.method == "POST":
        form = HouseListing(request.POST, instance=house_list)
        if form.is_valid():
            form.save()
            return redirect('view_house_listings.html')
    form = HouseListing(instance=house_list)
    return render(request, 'view_house_listing.html', {'form': form})
 
    
@login_required
def delete_house_listing(request, property_id):
    house_list = get_object_or_404(HouseListing, property_id=property_id, owner=request.user)
    if request.method == "POST":
        house_list.delete()
        return redirect('view_house_listings')
    return render(request, 'delete_house_listing.html', {'house_listing': house_list})
         
    