from Myapp.models import Users, Allergies, Requests
from rest_framework import serializers


class UsersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Users
        fields = ('url', 'name', 'email', 'contact_number', 'picture', 'password', 'address', 'city', 'postcode', 'terms_conditions', 'validations', 'company')

class AllergiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Allergies
        fields = ('url', 'ingredient')

class RequestsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Requests
        fields = ('url', 'food', 'picture', 'comment', 'temperature', 'time', 'name', 'contact_number', 'address', 'city','postcode','ingredient')

"""
Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. Serializers also provide deserialization, 
allowing parsed data to be converted back into complex types, after first validating the incoming data.
"""