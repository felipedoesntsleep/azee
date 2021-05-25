from http.server import BaseHTTPRequestHandler, HTTPServer
import time
from urllib.parse import parse_qs
import db
import json

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS, POST')
        self.send_header("Access-Control-Allow-Headers", "X-Requested-With")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/javascript")
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        # self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        
        print(self.path)
        split_ = self.path.split("/")[1:]
        print(split_)
        if (split_[0] == "games"):
            
            # print(split_[1])
            # db.insert_game(*split_[1:])
            # db.get_win_percent(split_[-1])
            self.wfile.write(bytes("<p>Request: %s</p>" % db.get_games(), "utf-8"))
        elif (split_[0] == "rung"):
            print(split_)
            db.get_rung(int(split_[1]))
        # self.wfile.write(bytes("<body>", "utf-8"))
        # self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        # self.wfile.write(bytes("</body></html>", "utf-8"))
    def do_POST(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        content_length = int(self.headers['Content-Length']) # <--- Gets the size of data
        # length = int(self.headers.getheader('content-length'))
        my_map = json.loads(self.rfile.read(content_length))
        # # print(post_data)
        # print(self.path)
        # my_map = parse_qs(post_data)
        # print(my_map)
        p1 = my_map['p1']
        p2 = my_map['p2']
        p3 = my_map['p3']
        p4 = my_map['p4']
        winner = my_map['winner']
        print(my_map)
        link = my_map['link']
        db.insert_game(p1, p2, p3, p4, winner, link)
if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")