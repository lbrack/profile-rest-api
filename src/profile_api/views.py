""""API View implementation
"""

from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Testing API view"""

    def get(self, request, format=None):
        """Returns a list of APIView features

        :param request:
        :param format:
        :return:
        """
        an_apiview = [
            "Uses HTTP verbs as functions (get, post, patch, put, delete)",
            "Is similar to traditional Django View",
            "Gives you the most control over your application logic",
            "is mapped manually to URLs",
            "Fakayu",
        ]
        return Response(dict(message="Hello", an_apiview=an_apiview))
