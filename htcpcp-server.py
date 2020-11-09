from http.server import HTTPServer, BaseHTTPRequestHandler

class Error(Exception):
    pass

class CoffeePotNotFound(Error):
    pass

class Serv(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/':
            self.path= '/index.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(200)
        except:
            file_to_open = "File not found"
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))

    def do_BREW(self):
        txt_headers = self.headers.as_string()
        try:
            if self.path != '/coffee':
                raise CoffeePotNotFound()

            if 'Content-Type: message/coffeepot coffee-message-body=start' in txt_headers:
                msg = 'Brew start successful.'
                #turn on coffee maker
                #if already on, return something else
            elif 'Content-Type: message/coffeepot coffee-message-body=stop' in txt_headers:
                msg = 'Brew stop successful.'
                #turn off coffee maker
                #if already off, return something else
            else:
                raise Exception()

            self.send_response(200)

        except CoffeePotNotFound:
            self.send_response(404)
            msg = 'Coffee pot not found.'

        except:
            self.send_response(400)
            msg = 'Bad request.'

        self.end_headers()
        self.wfile.write(bytes(msg, 'utf-8'))

    def do_POST(self):
        self.send_response(405)
        self.send_header('Allow', 'BREW, GET')
        self.end_headers()
        self.wfile.write(bytes('POST deprecated.', 'utf-8'))

htcpcpd = HTTPServer(('localhost', 8080), Serv)
htcpcpd.serve_forever()