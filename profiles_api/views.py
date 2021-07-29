from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    # this tells the view to expect a name of max_length 10 whenever doing post, put or patch request
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list of APIView features"""
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django view',
            'Gives you the most control over application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a Hello Msg with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self, request, pk=None):
        """Handle Updating an Object"""
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle partially updating an Object"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Handle deleting an Object"""
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automaticaly maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello', 'a_viewset': a_viewset})

    def create(self, request):
        """Create a new hello message"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """Handles the getting of an object by its ID"""
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handles the updating of an object by its ID"""
        return Response({'http_method': 'UPDATE'})

    def partial_update(self, request, pk=None):
        """Handles the updating part of an object by its ID"""
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handles the removing of an object by its ID"""
        return Response({'http_method': 'DELETE'})