from rest_framework import serializers 
from webapp.models import Users


class UsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ('uid',
                  'email',
                  'password')