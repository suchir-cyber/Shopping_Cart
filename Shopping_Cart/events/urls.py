from django.urls import path
from .views import add_membership, update_membership, membership_list, add_product, product_list

urlpatterns = [
    path('memberships/add/', add_membership, name='add_membership'),
    path('memberships/update/<int:membership_id>/', update_membership, name='update_membership'),
    path('memberships/', membership_list, name='membership_list'),
    path('products/add/', add_product, name='add_product'),
    path('products/', product_list, name='product_list'),
]