from django.http import HttpResponseNotFound
from django.shortcuts import get_object_or_404, render, redirect 
from django.contrib.auth.decorators import login_required
from .models import Listing, ListingImage, ListingVideo
from .forms import ListingForm, ListingImageFormSet, ListingVideoFormSet
from django.views.generic import TemplateView, ListView
from django.db.models import Q

# Create your views here.

def success_page(request):
    return render(request, "listingform/success_page.html")

@login_required
def create_listing(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        image_formset = ListingImageFormSet(request.POST, request.FILES, queryset=ListingImage.objects.none())
        video_formset = ListingVideoFormSet(request.POST, request.FILES, queryset=ListingVideo.objects.none())
        
        if form.is_valid() and image_formset.is_valid() and video_formset.is_valid():
            house_listing = form.save(commit=False)
            house_listing.owner = request.user
            house_listing.save()
            
            # Saving images and associating them with the house listing
            for image_form in image_formset:
                if image_form.cleaned_data:
                    pic = image_form.save(commit=False)
                    pic.listing = house_listing
                    pic.save()
                    
            # Saving videos and associating them with the house listing
            for video_form in video_formset:
                if video_form.cleaned_data:
                    vid = video_form.save(commit=False)
                    vid.listing = house_listing
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
    house_list = get_object_or_404(Listing, property_id=property_id)
    if request.method == "POST":
        house_list.delete()
        return redirect('home')
    return render(request, 'listingform/delete_house_listing.html', {'house_listing': house_list})

@login_required
def listing_details(request, property_id):
    images = ListingImage.objects.all()
    videos = ListingVideo.objects.all()
    try:
        listing = Listing.objects.get(property_id=property_id)
    except Listing.DoesNotExist:
        return HttpResponseNotFound("Listing not found")

    return render(request, "functions/view_aListing.html", {'listing': listing, 'images': images})
         
    
class SearchResultsView(ListView):
    model = Listing
    template_name = "functions/search_result.html"

    def get_queryset(self):  # new
        query = self.request.GET.get("q")
        object_list = Listing.objects.filter(
            Q(title__icontains=query) | Q(city__icontains=query) 
        )
        return object_list
    
