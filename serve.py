import os, http.server, socketserver
os.chdir(os.path.dirname(os.path.abspath(__file__)))
socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", 3000), http.server.SimpleHTTPRequestHandler) as s:
    print("Serving on port 3000")
    s.serve_forever()
