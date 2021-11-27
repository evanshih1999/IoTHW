from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
import json

# Create your views here.
class FibonacciView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        decoded = request.body.decode('utf-8')
        body = json.loads(decoded)
        order = body['order']
        return Response(data={ 'echo': 'Retrieving Fibonacci ' + str(order) }, status=200)

class LogsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):
        return Response(data={ 'echo': 'Retrieving Logs' }, status=200)
