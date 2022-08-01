from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class UserList(APIView):
    def get(self, request):
        return Response({'user': 'user'})

    def post(self, request):
        return null
