""""API View implementation
"""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profile_api import serializers

from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes


class HelloAPIView(APIView):
    """Testing API view"""

    # serializer_class = serializers.HelloSerializer

    # def __int__(self):
    #     self.pk = None

    @extend_schema(
        # extra parameters added to the schema
        parameters=None,
        # override default docstring extraction
        description="Returns a stupid message",
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
        examples=[
            OpenApiExample(
                "Example 1", description="Returns a pre-canned message", value="hello"
            ),
        ],
    )
    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            "Uses HTTP verbs as functions (get, post, patch, put, delete)",
            "Is similar to traditional Django View",
            "Gives you the most control over your application logic",
            "is mapped manually to URLs",
            "Fakayu",
        ]
        return Response(dict(message="Hello", an_apiview=an_apiview))

    @extend_schema(
        # extra parameters added to the schema
        parameters=None,
        # override default docstring extraction
        description="Pretends to update an object with no PK",
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
    )
    def put(self, request, pk=None):
        """Handle Updating an object"""
        self.pk = pk
        return Response(dict(method="PUT"), status=status.HTTP_200_OK)

    @extend_schema(
        # extra parameters added to the schema
        parameters=None,
        # override default docstring extraction
        description="Pretends to patch an object with no PK",
        # provide Authentication class
        # that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
    )
    def patch(self, request, pk=None):
        """Partial object of an object"""
        self.pk = pk
        return Response(dict(method="PATCH"), status=status.HTTP_200_OK)

    @extend_schema(
        # extra parameters added to the schema
        parameters=None,
        # override default docstring extraction
        description="Pretends to delete an object with no PK",
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
    )
    def delete(self, request, pk=None):
        """Partial object of an object"""
        self.pk = pk
        return Response(dict(method="DELETE"), status=status.HTTP_200_OK)

    @extend_schema(
        # extra parameters added to the schema
        parameters=[
            OpenApiParameter(
                name="name",
                description="whatever",
                required=True,
                type=serializers.HelloSerializer,
                examples=[
                    OpenApiExample(
                        "Example 1",
                        summary="short optional summary for example 1",
                        description="longer description for example 1",
                        value=dict(name="fakame"),
                    ),
                    OpenApiExample(
                        "Example 2",
                        summary="short optional summary for example 2",
                        description="longer description for example 2",
                        value=dict(name="fakayu2"),
                    ),
                ],
            ),
        ],
        # override default docstring extraction
        description="More descriptive text",
        # provide Authentication class that deviates from the views default
        auth=None,
        # change the auto-generated operation name
        operation_id=None,
        # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
        operation=None,
        # attach request/response examples to the operation.
    )
    def post(self, request):
        """Create a hello message with the name specified in parameter."""
        # serializer = self.serializer_class(data=request.data)
        serializer = serializers.HelloSerializer()
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"Fakayu {name}"
            return Response(dict(message=message))
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # The @extend_schema allows you to document the API according to the OpenAPI Spec.
    # @extend_schema(
    #     # extra parameters added to the schema
    #     parameters=[
    #         OpenApiParameter(
    #             name="artist", description="Filter by artist", required=False, type=str
    #         ),
    #         OpenApiParameter(
    #             name="release",
    #             type=OpenApiTypes.DATE,
    #             location=OpenApiParameter.QUERY,
    #             description="Filter by release date",
    #             examples=[
    #                 OpenApiExample(
    #                     "Example 1",
    #                     summary="short optional summary",
    #                     description="longer description",
    #                     value="1993-08-23",
    #                 ),
    #             ],
    #         ),
    #     ],
    #     # override default docstring extraction
    #     description="More descriptive text",
    #     # provide Authentication class that deviates from the views default
    #     auth=None,
    #     # change the auto-generated operation name
    #     operation_id=None,
    #     # or even completely override what AutoSchema would generate. Provide raw Open API spec as Dict.
    #     operation=None,
    #     # attach request/response examples to the operation.
    #     examples=[
    #         OpenApiExample(
    #             "Example 1", description="longer description", value="hello"
    #         ),
    #     ],
    # )
