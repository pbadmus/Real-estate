from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib.auth.decorators import login_required
from .models import Listing, ListingImage, ListingVideo
from .forms import ListingForm, ListingImageFormSet, ListingVideoFormSet

# Create your views here.

def success_page(request):
    return render(request, "listingform/success_page.html")

@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        image_form = ListingImageFormSet(request.POST, request.FILES, queryset=ListingImage.objects.none())
        video_form = ListingVideoFormSet(request.POST, request.FILES, queryset=ListingVideo.objects.none())
        if form.is_valid() and image_form.is_valid() and video_form.is_valid():
            house_listing = form.save()
            house_listing.owner = request.user
            house_listing.save()
            
            # For saving the image
            for image in image_form:
                if image.cleaned_data:
                    pic = image.save()
                    image.listing = house_listing
                    pic.save() 
                    
            for video in video_form:
                if video.cleaned_data:
                    vid = video.save(commit=False)
                    video.listing = house_listing
                    vid.save()
                    
            return redirect('home')
    else:
        form = ListingForm()
        image_formset = ListingImageFormSet(queryset=ListingImage.objects.none())
        video_formset = ListingVideoFormSet(queryset=ListingVideo.objects.none())
    return render(request, 'listingform/listingform.html', 
                    {'form': form,
                     'image_formset': image_formset,
                     'video_formset': video_formset,
                     })    


def view_listing(request):
    listings = Listing.objects.all()
    images = ListingImage.objects.all()
    videos = ListingVideo.objects.all()

    return render(request, 'listingform/view_listing.html', {
        'listings': listings,
        'images': images,
        'videos': videos,
    })


@login_required
def update_house_listing(request, property_id):
    house_list = get_object_or_404(Listing, property_id=property_id, owner=request.user)
    if request.method == "POST":
        form = Listing(request.POST, instance=house_list)
        if form.is_valid():
            form.save()
            return redirect('view_house_listings.html')
    form = Listing(instance=house_list)
    return render(request, 'view_house_listings.html', {'form': form})
 
    
@login_required
def delete_house_listing(request, property_id):
    house_list = get_object_or_404(Listing, property_id=property_id, owner=request.user)
    if request.method == "POST":
        house_list.delete()
        return redirect('view_house_listings')
    return render(request, 'delete_house_listing.html', {'house_listing': house_list})
         
    