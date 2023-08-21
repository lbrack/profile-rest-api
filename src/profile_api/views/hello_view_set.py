""""API View  set implementation

https://www.udemy.com/course/django-python/learn/lecture/6955028#content
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profile_api import serializers

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""

    def list(self, request):
        """List of object that the view represents"""
        an_viewset = [
            "Uses actions (list, create, retrieve, update, partial_update",
            "Automativally maps to URLs using routers",
            "Provide more functionalist with less code",
        ]
        return Response(dict(message="Hello", an_viewset=an_viewset))

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response(dict(http_method="GET -> retrieve"), status=status.HTTP_200_OK)

    def partial_update(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response(
            dict(http_method="PATCH -> partial_update"), status=status.HTTP_200_OK
        )

    def destroy(self, request, pk=None):
        """Handle getting an object by its ID"""
        return Response(
            dict(http_method="DELETE -> destroy"), status=status.HTTP_200_OK
        )

    def create(self, request):
        """Creates a new Hello message"""
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Viewset fakayu create::{name}!"
            return Response(dict(message=message))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
