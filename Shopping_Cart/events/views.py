from django.shortcuts import render, redirect
from .models import Membership, Product
from .forms import MembershipForm, ProductForm
from django.contrib.auth.decorators import login_required


@login_required
def add_membership(request):
    if request.method == 'POST':
        form = MembershipForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('membership_list')
    else:
        form = MembershipForm()
    return render(request, 'events/add_membership.html', {'form': form})


@login_required
def update_membership(request, membership_id):
    membership = Membership.objects.get(id=membership_id)
    if request.method == 'POST':
        form = MembershipForm(request.POST, instance=membership)
        if form.is_valid():
            form.save()
            return redirect('membership_list')
    else:
        form = MembershipForm(instance=membership)
    return render(request, 'events/update_membership.html', {'form': form})


@login_required
def membership_list(request):
    memberships = Membership.objects.all()
    return render(request, 'events/membership_list.html', {'memberships': memberships})


@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'events/add_product.html', {'form': form})


@login_required
def product_list(request):
    products = Product.objects.all()
    return render(request, 'events/product_list.html', {'products': products})