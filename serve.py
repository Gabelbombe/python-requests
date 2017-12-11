from BaseHTTPServer import BaseHTTPRequestHandler
from pathlib import Path
from random import randint

import json
import random

example = 'logs/example.json'

class GetHandler(BaseHTTPRequestHandler):

    # Slurp data from file
    def dummy_data(self):
        json_result = Path(example)

        if json_result.is_file():
            return json.load(open(example))

    # Return data or empty
    def random_selection(self):
        data = self.dummy_data()

        try:
            return random.sample(data, randint(1, len(data)+50))
        # Purposefully introduce entropy
        except ValueError:
            return ''

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(self.random_selection())
        return

if __name__ == '__main__':
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server at http://localhost:8080'


server.serve_forever()
