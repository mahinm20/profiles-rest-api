from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIViews(APIView):
    #Test APP


    def get(self,request,format=None):
        an_apiviews=[
            'Uses HTTP methods as functions like get, post,patch, put delete',
            'Is similar to tradional djanngo views',
            'Gives most control over app logic',
            'rick and morty',
        ]

        return Response({'messages':'Hello','an_apiviews':an_apiviews})
    