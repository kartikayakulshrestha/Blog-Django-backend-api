from django.urls import path, include
from api.views import UserViewSet,BlogViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'/users', UserViewSet)
router.register(r'/blog',BlogViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
]