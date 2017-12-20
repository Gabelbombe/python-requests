from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
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
        self.send_header('Content-Type', 'application/json')
        self.end_headers()

        self.wfile.write(json.dumps(self.random_selection()))
        return


def main():
    try:
        server = HTTPServer(('', 80), GetHandler)
        print '->> Starting server at http://127.0.0.1:80 and all patched hosts'
        server.serve_forever()
    except KeyboardInterrupt:
        print '->> Interrupt received; closing server socket'
        server.socket.close()

if __name__ == '__main__':
    main()
