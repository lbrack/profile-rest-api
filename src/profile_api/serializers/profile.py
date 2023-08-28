""" A serializer allows you to format the input of a request as a python object.

"""

from rest_framework import serializers
from profile_api import models  # Import the model


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "password")
        extra_kwargs = dict(
            password=dict(write_only=True, style=dict(input_type="password"))
        )

    def create(self, validated_data):
        """Creates and returns a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data["email"],
            name=validated_data["name"],
            password=validated_data["password"],
        )
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if "password" in validated_data:
            password = validated_data.pop("password")
            instance.set_password(password)

        return super().update(instance, validated_data)
