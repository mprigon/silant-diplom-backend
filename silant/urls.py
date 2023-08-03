"""
URL configuration for silant project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include, re_path
from django.views.generic import TemplateView

from loaderapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('swagger-ui/', TemplateView.as_view(
          template_name='swagger-ui.html',
          extra_context={'schema_url': 'openapi-schema'}
          ), name='swagger-ui'),

    path('api/v1/loaderlist/', LoaderAPIList.as_view()),
    path('api/v1/loaderdetail/<int:pk>/', LoaderAPIDetailView.as_view()),
    path('api/v1/loaderupdate/<int:pk>/', LoaderAPIUpdate.as_view()),
    path('api/v1/loaderdelete/<int:pk>/', LoaderAPIDestroy.as_view()),

    path('api/v1/techservicelist/', TechServiceAPIList.as_view()),
    path('api/v1/techservicedetail/<int:pk>/', TechServiceAPIDetailView.as_view()),
    path('api/v1/techserviceupdate/<int:pk>/', TechServiceAPIUpdate.as_view()),
    path('api/v1/techservicedelete/<int:pk>/', TechServiceAPIDestroy.as_view()),

    path('api/v1/claimslist/', ClaimsAPIList.as_view()),
    path('api/v1/claimsdetail/<int:pk>/', ClaimsAPIDetailView.as_view()),
    path('api/v1/claimsupdate/<int:pk>/', ClaimsAPIUpdate.as_view()),
    path('api/v1/claimsdelete/<int:pk>/', ClaimsAPIDestroy.as_view()),

    path('api/v1/modelloaderlist/', ModelLoaderAPIList.as_view()),
    path('api/v1/modelloaderdetail/<int:pk>/', ModelLoaderAPIDetailView.as_view()),
    path('api/v1/modelloaderupdate/<int:pk>/', ModelLoaderAPIUpdate.as_view()),
    path('api/v1/modelloaderdelete/<int:pk>/', ModelLoaderAPIDestroy.as_view()),


    path('', HomePageView.as_view(), name='home_page'),

]
