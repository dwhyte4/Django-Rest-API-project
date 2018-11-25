from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json

from rest_framework import viewsets
from Myapp.models import Users, Allergies, Requests
from Myapp.serializers import UsersSerializer, AllergiesSerializer, RequestsSerializer

class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Users.objects.all().order_by('-date_joined')
    serializer_class = UsersSerializer

class AllergiesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Allergies.objects.all().order_by('-date_joined')
    serializer_class = AllergiesSerializer

class RequestsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Requests.objects.all().order_by('-date_joined')
    serializer_class = RequestsSerializer    

# Create your views here.

def login(request):
    return JsonResponse("Reached login endpoint")

def register(request):
    return JsonResponse("Reached register endpoint")

def getAccountDetails(request, account_id=None):
    if account_id is None:
        return JsonResponse({
            "success": False,
            "reason": "No account ID"
        })

    return JsonResponse("Reached account-details endpoint")

def updateAccountDetails(request, account_id=None):
    if account_id is None:
        return JsonResponse({
            "success": False,
            "reason": "No account ID"
        })

    return JsonResponse("Reached update-account endpoint")

def getRequests(request, account_id=None):
    if account_id is None:
        return JsonResponse({
            "success": False,
            "reason": "No account ID"
        })

    return JsonResponse("Reached requests endpoint (for food that is...)")

