from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Mensajes

class MensajeslistSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""
    #sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    sender = serializers.ReadOnlyField(source='sender.username') # ADD THIS LINE

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Mensajes
        fields = ('message', 'date_sent','sender','receiver')

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    """For Serializing User"""
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password']
