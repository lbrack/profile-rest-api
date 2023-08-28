""" A serializer allows you to format the input of a request as a python object.

"""

from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView."""

    name = serializers.CharField(max_length=10)
