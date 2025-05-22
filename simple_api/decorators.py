from typing import Callable
from functools import wraps


class EndpointRegistry:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.endpoints = []
        return cls._instance

    def register(self, path: str, method: str):
        def decorator(func: Callable):
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            wrapper._endpoint = (path, method)
            self.endpoints.append(wrapper)
            return wrapper
        return decorator


def endpoint(path: str, method: str = 'GET'):
    registry = EndpointRegistry()
    return registry.register(path, method)
