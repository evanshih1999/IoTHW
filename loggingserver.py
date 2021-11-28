import os
import os.path as osp
import sys
BUILD_DIR = osp.join(osp.dirname(osp.abspath(__file__)), "build/service/")
sys.path.insert(0, BUILD_DIR)
import argparse

import grpc
from concurrent import futures
import log_pb2
import log_pb2_grpc

import psutil
import paho.mqtt.client as mqtt

history = []

class LogCalculatorServicer(log_pb2_grpc.LogCalculatorServicer):

    def __init__(self):
        pass

    def Compute(self, request, context):

        response = log_pb2.LogResponse()
        response.history.extend(history)

        return response

def on_message(client, obj, msg):
    order = str(msg.payload)
    order = order[2:-1]
    print(order)
    history.append(int(order))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", default="0.0.0.0", type=str)
    parser.add_argument("--port", default=8080, type=int)
    args = vars(parser.parse_args())

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    servicer = LogCalculatorServicer()
    log_pb2_grpc.add_LogCalculatorServicer_to_server(servicer, server)

    client = mqtt.Client()
    client.on_message = on_message
    client.connect(host='127.0.0.1', port=1883)
    client.subscribe('order', 0)

    try:
        client.loop_start()
        server.add_insecure_port(f"{args['ip']}:{args['port']}")
        server.start()
        print(f"Run gRPC Server at {args['ip']}:{args['port']}")
        server.wait_for_termination()
    except KeyboardInterrupt:
        client.loop_stop()