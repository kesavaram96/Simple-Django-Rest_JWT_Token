from rest_framework import exceptions, serializers
from django.contrib.auth import get_user_model

User=get_user_model()
class loginserializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields =('username','password')
        