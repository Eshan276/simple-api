from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from typing import Any, Dict
from urllib.parse import parse_qs, urlparse


class RequestHandler(BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.api = kwargs.pop('api', None)
        super().__init__(*args, **kwargs)

    def _send_response(self, data: Any, status: int = 200):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def _handle_request(self):
        path = urlparse(self.path).path
        handler = self.api.get_handler(path, self.command)

        if handler is None:
            self._send_response({'error': 'Not Found'}, 404)
            return

        # Parse request data
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length > 0 else b''

        try:
            data = json.loads(body) if body else {}
        except json.JSONDecodeError:
            data = {}

        # Execute handler
        try:
            result = handler(data)
            self._send_response(result)
        except Exception as e:
            self._send_response({'error': str(e)}, 500)

    def do_GET(self):
        self._handle_request()

    def do_POST(self):
        self._handle_request()

    def do_PUT(self):
        self._handle_request()

    def do_DELETE(self):
        self._handle_request()


def run_server(api, host: str, port: int=6969):
    def handler(*args):
        RequestHandler(api=api, *args)

    server = HTTPServer((host, port), handler)
    print(f"Server started on http://{host}:{port}")

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        server.server_close()
        print("\nServer stopped")
