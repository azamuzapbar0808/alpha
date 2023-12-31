from api.restaurant.views import RestaurantViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register("", RestaurantViewSet, basename="restaurant")

urlpatterns = [
    path("", include(router.urls)),
]