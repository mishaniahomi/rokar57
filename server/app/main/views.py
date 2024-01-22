from django.shortcuts import render
from rest_framework import generics

from .models import Banner
from .serializers import BannerSerializer


class BannerViewSet(generics.ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer


# Create your views here.
def index(request):
    return render(request, 'main/index.html')