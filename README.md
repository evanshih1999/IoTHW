# IoTHW

## How to run
- Install project dependencies
```bash
$ pip3 install -r requirements.txt
```
- Run the backend server
```bash
$ python3 server.py runserver 0.0.0.0:8000
```

## Using `curl` to perform client request
```bash
$ curl http://localhost:8000/rest/fibonacci
```
Or you can use `http` to send request
```bash
$ sudo apt-get install httpie
$ http --json http://localhost:8000/rest/fibonacci
```