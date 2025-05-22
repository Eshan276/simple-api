from simple_api import SimpleAPI, endpoint

# Create an API instance
api = SimpleAPI("MyAPI")

# Define endpoints using decorators


@endpoint("/hello", method="GET")
def hello(data):
    return {"message": "Hello, World!"}


@endpoint("/echo", method="POST")
def echo(data):
    return {"received": data}


# Add endpoints to the API
api.add_endpoint("/hello", "GET", hello)
api.add_endpoint("/echo", "POST", echo)

# Run the server
if __name__ == "__main__":
    api.run(host="localhost", port=8000)
