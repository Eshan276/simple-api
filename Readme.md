# simple-api

A simple API framework for creating local APIs in Python.

## Update
> **pypi launch INCOMING** 🚀


## Features

- Minimal setup for defining API endpoints
- Decorator-based endpoint registration
- Built-in HTTP server for local development

## Installation

Clone the repository and install with pip:

```sh
pip install .
```

## Usage

Create a new API and define endpoints using the `@endpoint` decorator:

```python
from simple_api import SimpleAPI, endpoint

api = SimpleAPI("MyAPI")

@endpoint("/hello", method="GET")
def hello(data):
    return {"message": "Hello, World!"}

@endpoint("/echo", method="POST")
def echo(data):
    return {"received": data}

api.add_endpoint("/hello", "GET", hello)
api.add_endpoint("/echo", "POST", echo)

if __name__ == "__main__":
    api.run(host="127.0.0.1", port=8000)
```



## License

MIT License