from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm

@login_required
def user_products(request):
    """عرض منتجات المستخدم الحالي"""
    products = Product.objects.filter(user=request.user)
    return render(request, 'userproducts/user_products.html', {'products': products})

@login_required
def add_product(request):
    """إضافة منتج جديد"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user  # ✅ تعديل هنا
            product.save()
            return redirect('userproducts:user_products')
    else:
        form = ProductForm()
    return render(request, 'userproducts/add_product.html', {'form': form})
