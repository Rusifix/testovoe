"""testovoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from products.views import CreateCheckoutSessionView, ProductsLandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProductsLandingPageView.as_view(), name='landing-page'),
    # path('orders/add/<int:item_id>/', orders_add, name='orders_add'),
    # path('orders/remove/<int:id>/', orders_remove, name='orders_remove'),
    path('create-checkout-session/<pk>/', CreateCheckoutSessionView.as_view(), name='create-checkout-session')
]
