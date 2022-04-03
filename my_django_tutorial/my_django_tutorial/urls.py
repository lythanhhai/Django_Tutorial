"""my_django_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pages import views as viewPages
from products import views as viewProducts

urlpatterns = [
    path('', viewPages.homepage_view, name="home"),
    path('contact/', viewPages.contact_view, name="contact"),
    path('about/', viewPages.about_view, name="about"),
    path('social/', viewPages.social_view, name="social"),
    path('product/', viewProducts.product_detail_view, name="detail"),
    path('product/create/', viewProducts.product_create_view, name="create"),
    path('product/<int:id>/', viewProducts.dynamic_url_view, name="detail_item"),
    path('product/<int:id>/delete/', viewProducts.product_delete_view, name="delete_view"), 
    path('admin/', admin.site.urls),
]
