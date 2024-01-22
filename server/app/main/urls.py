from django.urls import path
from .views import index, BannerViewSet

urlpatterns = [
   path('', index, name='index'),
   path('api/getbanners', BannerViewSet.as_view(), name='getbanners'),
]
