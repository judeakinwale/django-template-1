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


app_name = "main"

urlpatterns = [
    path("", views.HomeListView.as_view(), name="home"),
    path("s/", views.SearchListView.as_view(), name="search"),
    path("items/", views.ItemListView.as_view(), name="items"),
    path("items/create/", views.ItemCreateView.as_view(), name="item_create"),
    path("items/<slug>/", views.ItemDetailView.as_view(), name="item_detail"),
    path("items/<slug>/update", views.ItemUpdateView.as_view(), name="item_update"),
    path("items/<slug>/delete", views.ItemDeleteView.as_view(), name="item_delete"),
]
