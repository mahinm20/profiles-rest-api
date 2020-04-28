from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import serializers
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings 

class HelloAPIViews(APIView):
    #Test APP
    serializer_class = serializers.HelloSerializer #object of serializer class 

    def get(self,request,format=None):
        an_apiviews=[
            'Uses HTTP methods as functions like get, post,patch, put delete',
            'Is similar to tradional djanngo views',
            'Gives most control over app logic',
            'rick and morty',
        ]

        return Response({'message':'Hello','an_apiviews':an_apiviews})



    def post(self,request):
        serializers=self.serializer_class(data=request.data) #Retrive data sent in the request 


        if serializers.is_valid(): #  To check if the conditions are valid 
            name = serializers.validated_data.get('name')
            message = f'Hello {name}' #Format string
            return Response({'message':message})
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)    


    def put(self,request,pk=None):
        #Update
        return Response({'method':'PUT'})
            #name = serializers.validated_data.get('name')
            #message = f'Hello {name}' #Format string
            #return Response({'message':message})
        # serializers=self.serializer_class(data=request.data) #Retrive data sent in the request 


        # if serializers.is_valid(): #  To check if the conditions are valid 
        #     name = serializers.validated_data.get('name')
        #     message = f'Hello {name}' #Format string
        #     return Response({'message':message})
        # else:
        #     return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    
    def patch(self,request,pk=None):
        #Update
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        #Update
        return Response({'method':'DELETE'})        


class HelloViewSet(viewsets.ViewSet):

    serializer_class = serializers.HelloSerializer #object of serializer class 

    def list(self,request):

        a_viewset = [
            'Uses actions (list, create, retrieve, update, partial_update)',
            'Automatically maps to URLS using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': 'Hello!','a_viewset': a_viewset})

    def create(self , request, pk=None):
        serializers=self.serializer_class(data=request.data) #Retrive data sent in the request 


        if serializers.is_valid(): #  To check if the conditions are valid 
            name = serializers.validated_data.get('name')
            message = f'Hello {name}' #Format string
            return Response({'message':message})
        else:
            return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)    

    def retrieve(self, request, pk=None):
        """Handle getting an object by its ID"""

        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """Handle updating an object"""

        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        """Handle updating part of an object"""

        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        """Handle removing an object"""

        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserProfileSerializers
    queryset = models.UserProfile.objects.all()
   
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)



class UserLoginApiView(ObtainAuthToken):
   """Handle creating user authentication tokens"""
   renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES




        



    