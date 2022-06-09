"""config URL Configuration

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
# from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic.base import RedirectView

import os

app_list = os.getenv("APP_LIST", "").split(",")
api_version = "v1"

urlpatterns = [
    path("", RedirectView.as_view(url=f"/api/{api_version}/")),
    # path("admin/", admin.site.urls),
    path(f"api/{api_version}/rest-auth/", include("rest_framework.urls")),
    path(f"api/{api_version}/rest-auth/", include("rest_auth.urls")),
    path(f"api/{api_version}/rest-auth/registration/", include("rest_auth.registration.urls")),
]

if "coin" in app_list:
    from coin.urls import router as coin_router

    urlpatterns.extend([path(rf"api/{api_version}/", include(coin_router.urls))])
    urlpatterns.extend([path(f"api/{api_version}/", include("coin.urls"))])

if "payment" in app_list:
    from payment.urls import router as payment_router

    urlpatterns.extend([path(r"api/v1/", include(payment_router.urls))])
