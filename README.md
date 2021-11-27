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

## Ask for the result of fibonacci at N order
```bash
$ curl -X POST http://localhost:8000/rest/fibonacci 
    -d '{"order":N}'
```

## Get a list of history fibonacci requests sent before
```bash
$ curl http://localhost:8000/rest/logs
```