from rest_framework import serializers
from .models import UserDetails


# class UserDetailsSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=100)
#     email = serializers.EmailField()
#     password = serializers.CharField(max_length=100)

#model serializer for UserDetails model
class UserDetailsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDetails
        fields = ['username', 'email', 'password']