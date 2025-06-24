from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from listings.models import Listing
from listings.forms import ListingForm

# عرض المنتجات الخاصة بالمستخدم
@login_required
def user_products(request):
    products = Listing.objects.filter(owner=request.user).order_by('-created_at')
    return render(request, 'userproducts/user_products.html', {'products': products})


# إضافة منتج جديد مرتبط بالمستخدم
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ListingForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            return redirect('userproducts:user_products')
    else:
        form = ListingForm()

    return render(request, 'userproducts/add_product.html', {'form': form})
