from django.urls import path
from .views import (
 HomePageView,
 Map, 
 Str1762,
 Str1710R,
 Str1710Sk,
 Str1710Si,
 Str1710Os,
 Str1710Me,
 Str1801,
 Str1802,
)

urlpatterns=[
    path('', HomePageView.as_view(), name = 'home'),
    path('map/', Map.as_view(), name = 'map'),
    path('1762/', Str1762.as_view(), name = 'str1762'),
    path('1710Re/', Str1710R.as_view(), name = 'str1710Re'),
    path('1710Sk/', Str1710Sk.as_view(), name = 'str1710Sk'),
    path('1710Si/', Str1710Si.as_view(), name = 'str1710Si'),
    path('1710Me/', Str1710Me.as_view(), name = 'str1710Me'),
    path('1710Os/', Str1710Os.as_view(), name = 'str1710Os'),
    path('1801/', Str1801.as_view(), name = 'str1801'),
    path('1802/', Str1802.as_view(), name = 'str1802'),
]