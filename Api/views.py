#from django.shortcuts import render
from rest_framework.views import APIView
from models import *
from rest_framework.response import Response
from rest_framework import authentication,permissions
from pony.orm import db_session
# Create your views here.


class UserRestView(APIView):
    permission_classes = (permissions.AllowAny,)

    @db_session
    def get(self,request, format=None):
        rest_users = User.select()
        return Response(rest_users,status=200)
    