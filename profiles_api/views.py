from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

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
        #return Response({'method':'PUT'})
            #name = serializers.validated_data.get('name')
            #message = f'Hello {name}' #Format string
            return Response({'message':message})
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

        



    