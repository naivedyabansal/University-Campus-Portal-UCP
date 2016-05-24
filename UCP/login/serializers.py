from rest_framework import serializers
from django.contrib.auth.models import User
from login.models import UserProfile

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'password')
        write_only_fields = ('password',)
        read_only_fields = ('id',)
    
    def create(self, validated_data):
        user = User(email=validated_data['email'], username=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate_email(self, value):
        """
        Check if user with this email already exists
        """
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email ID already registered")
        return value


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'first_name', 'last_name', 'designation', 'profile_image')
        read_only_fields = ('id',)
