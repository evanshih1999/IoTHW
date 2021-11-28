from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
import json

import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "../build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
import fib_pb2
import fib_pb2_grpc
import log_pb2
import log_pb2_grpc

import psutil
import paho.mqtt.client as mqtt

# Create your views here.
class FibonacciView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        decoded = request.body.decode('utf-8')
        body = json.loads(decoded)
        order = body['order']

        client = mqtt.Client()
        client.connect(host='127.0.0.1', port=1883)
        client.loop_start()
        client.publish(topic='order', payload=order)
        client.loop_stop()

        host = f"{'127.0.0.1'}:{'8080'}"
        print(host)
        with grpc.insecure_channel(host) as channel:
            stub = fib_pb2_grpc.FibCalculatorStub(channel)

            request = fib_pb2.FibRequest()
            request.order = order

            response = stub.Compute(request)
            print(response.value)
        
        return Response(data={ response.value }, status=200)

class LogsView(APIView):
    permission_classes = (permissions.AllowAny,)

    def get(self, request):

        host = f"{'127.0.0.1'}:{'8888'}"
        print(host)
        with grpc.insecure_channel(host) as channel:
            stub = log_pb2_grpc.LogCalculatorStub(channel)

            request = log_pb2.LogRequest()

            response = stub.Compute(request)
            print(response.history)
        
        return Response(data={ 'history': response.history[:] }, status=200)
