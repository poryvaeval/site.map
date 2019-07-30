from django.urls import path
from .views import HomePageView, Map

urlpatterns=[
    path('', HomePageView.as_view(), name = 'home'),
    path('map/', Map.as_view(), name = 'map'),
]