# IoTHW

## How to run
- Install project dependencies
```bash
# Install protobuf compiler
$ sudo apt-get install protobuf-compiler

# Install buildtools
$ sudo apt-get install build-essential make

# Install python packages
$ pip3 install -r requirements.txt
```
- Compile protobuf schema to python wrapper
```bash
$ make
```

- Start the gRPC services
```bash
$ python3 fibonacci.py --ip 0.0.0.0 --port 8080
$ python3 loggingserver.py --ip 0.0.0.0 --port 8888
```

- Run the backend server
```bash
$ python3 server.py runserver 0.0.0.0:8000
```

## Ask for the result of fibonacci at N order
```bash
$ curl -X POST http://localhost:8000/rest/fibonacci 
    -d '{"order":N}'
```

## Get a list of history fibonacci requests sent before
```bash
$ curl http://localhost:8000/rest/logs
```