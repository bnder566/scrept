from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Listing
from .forms import ListingForm

# عرض كل الإعلانات
def listing_list(request):
    listings = Listing.objects.filter(status='approved').order_by('-created_at')
    return render(request, 'listings/listing_list.html', {'listings': listings})

# إنشاء إعلان جديد
def create_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.status = 'pending'  # يتم وضعه كمعلّق تلقائيًا
            listing.save()
            return redirect('listing_list')
    else:
        form = ListingForm()
    return render(request, 'listings/create_listing.html', {'form': form})


# ✅ للمشرف: عرض الإعلانات قيد المراجعة
@staff_member_required
def pending_listings(request):
    listings = Listing.objects.filter(status='pending')
    return render(request, 'listings/admin_pending_listings.html', {'listings': listings})

# ✅ للمشرف: قبول إعلان
@staff_member_required
def approve_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing.status = 'approved'
    listing.save()
    return redirect('listings:pending_listings')

# ✅ للمشرف: رفض إعلان
@staff_member_required
def reject_listing(request, pk):
    listing = get_object_or_404(Listing, pk=pk)
    listing.status = 'rejected'
    listing.save()
    return redirect('listings:pending_listings')
