import requests
from .models import *
from .serializers import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate
import threading
import time


class CrudAPIView(APIView):
    permission_classes = [permissions.AllowAny]
    def get(self, request, pk=''):
        if pk == '':
            dados = Crud.objects.all()
            serializer = CrudSerializer(dados, many=True)
            return Response(serializer.data)
        else:
            dados = Crud.objects.get(id=pk)
            serializer = CrudSerializer(dados)
            return Response(serializer.data)

    def put(self, request, pk=''):
        dados = Crud.objects.get(id=pk)
        serializer = CrudSerializer(dados, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk=''):
        dados = Crud.objects.get(id=pk)
        dados.delete()
        return Response({"msg": "Apagado com sucesso"})

    def post(self, request):
        serializer = CrudSerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
