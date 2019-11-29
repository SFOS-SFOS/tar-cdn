#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import os

PORT_NUMBER = 80

#This class will handles any incoming request from
#the browser
class myHandler(BaseHTTPRequestHandler):

        #Handler for the GET requests
        def do_GET(self):
                self.send_response(200)
                self.send_header('Content-type','text/html')
                self.end_headers()

                # Send the html message

                #self.wfile.write("Arr from " + os.popen('curl ipinfo.io/ip').read().replace('\n',''))
                #self.wfile.write("<br><br>")
                #self.wfile.write(os.popen('curl ipinfo.io').read().replace('\n',''))
                f = open("~/server/index.html", 'rb')
                self.wfile.write(f.read())
                f.close()
                return

try:
        #Create a web server and define the handler to manage the
        #incoming request
        server = HTTPServer(('', PORT_NUMBER), myHandler)
        print 'Started httpserver on port ' , PORT_NUMBER

        #Wait forever for incoming htto requests
        server.serve_forever()

except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
