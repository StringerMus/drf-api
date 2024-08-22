"""drf_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from .views import root_route, logout_route

urlpatterns = [
    path('', root_route),  # Root route
    path('admin/', admin.site.urls),  # Admin route
    path('api-auth/', include('rest_framework.urls')),  # DRF login/logout
    path('dj-rest-auth/logout/', logout_route),  # Custom logout route
    path('dj-rest-auth/', include('dj_rest_auth.urls')),  # DJ Rest Auth routes
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),  # DJ Rest Auth registration
    path('accounts/', include('allauth.urls')),  # Allauth routes for account management
    path('', include('profiles.urls')),  # Profile routes
    path('', include('posts.urls')),  # Post routes
    path('', include('comments.urls')),  # Comment routes
    path('', include('likes.urls')),  # Like routes
    path('', include('followers.urls')),  # Follower routes
]