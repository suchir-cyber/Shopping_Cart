from django.shortcuts import render, redirect
from .models import Product, Membership
from .forms import ProductForm, MembershipForm
from accounts.models import Vendor
from django.contrib.auth.decorators import login_required

@login_required
def vendor_dashboard(request):
    products = Product.objects.filter(vendor__user=request.user)
    return render(request, 'events/vendor_dashboard.html', {'products': products})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = Vendor.objects.get(user=request.user)
            product.save()
            return redirect('vendor_dashboard')
    else:
        form = ProductForm()
    return render(request, 'events/add_product.html', {'form': form})

@login_required
def user_dashboard(request):
    memberships = Membership.objects.filter(user=request.user)
    return render(request, 'events/user_dashboard.html', {'memberships': memberships})