import http.server
import socketserver

PORT = 8000

# Set up the server handler
Handler = http.server.SimpleHTTPRequestHandler

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Local server started at: http://localhost:{PORT}")
        print("Press CTRL+C to stop the server.")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped successfully.")
