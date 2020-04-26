from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    # Serializer a name field for testing api

    name= serializers.CharField(max_length=10)


class UserProfileSerializers(serializers.ModelSerializer):
    #Serial a use profile method
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user    





    # class Meta:
    #     model = models.UserProfile
    #     fields = ('id','name','email','password')

    #     #For password safety 
    #     extra_kwargs = {
    #         'password': {
    #             'write_only': True,
    #             'style': {'input_type': 'password'}
    #         }
    #     }

    # def create(self, validated_data):

    #     #Create and return new user

    #     user= models.UserProfile.objects.create_user(
    #         email=validated_data['email'],
    #         name=validated_data['name'],
    #         password=validated_data['password']
    #     )


    #     return user
