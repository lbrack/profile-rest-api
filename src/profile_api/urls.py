from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_api import views

router = DefaultRouter()
# basename is used to retrieve the URL in our router (by name)
router.register("hello-viewset", views.HelloViewSet, basename="hello-viewset")

urlpatterns = [
    path("hello-view", views.HelloAPIView.as_view()),
    path("", include(router.urls)),
]
