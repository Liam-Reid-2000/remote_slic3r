from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import os

# import requests
UPLOAD_DIRECTORY = "uploads"

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
      content_length = int(self.headers['Content-Length'])
      data = self.rfile.read(content_length)

      # Ensure the uploads directory exists
      if not os.path.exists(UPLOAD_DIRECTORY):
          os.makedirs(UPLOAD_DIRECTORY)

      filepath = os.path.join(UPLOAD_DIRECTORY, "upload.obj")

      with open(filepath, 'wb') as f:
          f.write(data)
          
      # command = "cd .. && cd Slic3r && slic3r-console --load config.ini C:\\Users\\Microwave\\remote_slic3r\\uploads\\upload.obj"
      command = "cd Slic3r && ./Slic3r --load /app/config.ini --scale 20 /app/uploads/upload.obj"

      result = os.system(command)
      
      with open("/app/uploads/upload.gcode", 'rb') as f:
          output_data = f.read()

      self.send_response(200)
      self.send_header('Content-Length', len(output_data))
      self.end_headers()
      self.wfile.write(output_data)


            
port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', port), RequestHandler)
    server.serve_forever()