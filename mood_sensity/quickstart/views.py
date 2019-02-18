from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, PictureSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.gis.measure import D
from django.contrib.gis.geos import *

from .models import Picture

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

# ViewSets define the view behavior.
class PictureViewSet(viewsets.ModelViewSet):
    serializer_class = PictureSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Picture.objects.all().filter(user=request.user)
        #Get the current location for the user
        pnt = fromstr('POINT(48.796777 2.371140 )', srid=4326)
        #Compare the location using the longitude and latitude stored in the db with geodjango
        queryset = Picture.objects.filter(point__distance_lte=(pnt, D(km=20)))
        return queryset