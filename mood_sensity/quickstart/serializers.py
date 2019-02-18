from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Picture
from quickstart.detect_faces import detect_faces


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class PictureSerializer(serializers.ModelSerializer):
    class Meta():
        model = Picture
        fields = ('picture', 'latitude', 'longitude', 'timestamp', 'mood')

    def current_location():
        send_url = 'http://api.ipstack.com/177.245.200.30?access_key=f4422326475b6edb7ed6caf6a56a1694'
        r = requests.get(send_url)
        j = json.loads(r.text)
        lat = j['latitude']
        lon = j['longitude']
        return lat, lon

    def create(self, validated_data):
        #Upload the picture
        picture = validated_data.get('picture')
        #detect the faces using the function available in detect_faces.py using the uploaded picture for detrcting the face
        detect_faces(picture)
        mood = validated_data.get('mood')
        #save(latitude='',longitude='', mood='')
        location = self.current_location()
        return Picture.objects.create(picture = picture,latitude=location[0],longitude=location[1], mood=mood)