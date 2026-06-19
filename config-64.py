#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler
import urllib.request
import ssl

class ProxyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = self.path[1:]  # Remove leading /
        if not url.startswith('http'):
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Usage: /https://example.com')
            return
        
        try:
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            })
            
            with urllib.request.urlopen(req, context=ctx, timeout=10) as response:
                self.send_response(response.status)
                for header, value in response.headers.items():
                    if header.lower() not in ['transfer-encoding', 'content-encoding']:
                        self.send_header(header, value)
                self.end_headers()
                self.wfile.write(response.read())
                
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

if __name__ == '__main__':
    server = HTTPServer(('0.0.0.0', 8080), ProxyHandler)
    print('Proxy running on port 8080')
    server.serve_forever()
