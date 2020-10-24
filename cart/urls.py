"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views


app_name = "cart"

urlpatterns = [
    path("cart/", views.OrderListView.as_view(), name="cart"),
    path("cart/add/<slug>/", views.add_to_cart, name="add_to_cart"),
    path("cart/remove/<slug>/", views.remove_from_cart, name="remove_from_cart"),
    path("cart/remove-single/<slug>/", views.remove_single_item_from_cart, name="remove_single_item_from_cart"),
    path("checkout/", views.CheckoutView.as_view(), name="checkout"),
]
