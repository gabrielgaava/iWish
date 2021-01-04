# Django Imports
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

# API ViewSets
from wish.api.viewsets import WishListViewSet, WishViewSet
from account.api.viewsets import UserViewSet

# API Endpoints:
router = routers.DefaultRouter()
router.register(r'wishlist', WishListViewSet)
router.register(r'wish', WishViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
