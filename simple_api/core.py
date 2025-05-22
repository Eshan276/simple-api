import json
from typing import Callable, Dict, Any, Optional
from .decorators import EndpointRegistry


class SimpleAPI:
    def __init__(self, name: str):
        self.name = name
        self.endpoints: Dict[str, Dict[str, Callable]] = {}

    def add_endpoint(self, path: str, method: str, handler: Callable):
        if path not in self.endpoints:
            self.endpoints[path] = {}
        self.endpoints[path][method.upper()] = handler

    def get_handler(self, path: str, method: str) -> Optional[Callable]:
        return self.endpoints.get(path, {}).get(method.upper())

    def run(self, host: str = 'localhost', port: int = 8000):
        from .server import run_server
        run_server(self, host, port)
