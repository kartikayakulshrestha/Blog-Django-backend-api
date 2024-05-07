from django.urls import path, include
from api.views import UserViewSet,BlogViewSet,userv2ViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'/users', UserViewSet)
router.register(r'/blog',BlogViewSet)
router.register(r'/users1',userv2ViewSet,basename="_v2_")

urlpatterns = [
    path('', include(router.urls)),
    
]