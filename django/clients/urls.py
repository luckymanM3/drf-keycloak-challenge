from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, MyView

router = DefaultRouter()
router.register(r'clients', ClientViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('endpoint/', MyView.as_view()),
]