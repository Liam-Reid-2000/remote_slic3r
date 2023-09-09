from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import os

# import requests

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
      
      command = "cd Slic3r && ./Slic3r --help"

      output = os.popen(command).read()
      
      self.send_response(200)
      self.send_header("Content-type", "application/json")
      self.send_header('Access-Control-Allow-Origin', '*')
      self.end_headers()
      self.wfile.write(json.dumps({'output':output}).encode())
      return
    
    def do_POST(self):
      self.send_response(200)
      self.send_header('Content-type', 'text/plain')
      self.end_headers()

            

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 5000), RequestHandler)
    server.serve_forever()