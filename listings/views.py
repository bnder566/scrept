from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm

# عرض كل الإعلانات
def listing_list(request):
    listings = Listing.objects.all().order_by('-created_at')
    return render(request, 'listings/listing_list.html', {'listings': listings})

# إنشاء إعلان جديد
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listing_list')
    else:
        form = ListingForm()
    return render(request, 'listings/create_listing.html', {'form': form})
