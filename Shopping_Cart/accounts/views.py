from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm, VendorRegistrationForm
from .models import Vendor

def home(request):
    return render(request, 'accounts/home.html')

def register_user(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register_user.html', {'form': form})

def register_vendor(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        vendor_form = VendorRegistrationForm(request.POST)
        if user_form.is_valid() and vendor_form.is_valid():
            user = user_form.save()
            vendor = vendor_form.save(commit=False)
            vendor.user = user
            vendor.save()
            login(request, user)
            return redirect('vendor_dashboard')
    else:
        user_form = UserRegistrationForm()
        vendor_form = VendorRegistrationForm()
    return render(request, 'accounts/register_vendor.html', {'user_form': user_form, 'vendor_form': vendor_form})