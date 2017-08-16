import http.server
import Control_Panel

class Handler( http.server.BaseHTTPRequestHandler):

    
    def do_GET( self ): # Reading
        if self.path=="/download":
            self.send_response(200)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            message = "Hello world!"
            print("Hello world!")
            self.wfile.write(bytes(message, "utf8"))
            
        else:
            self.send_response(404)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            message = "Unknown Request"
            self.wfile.write(bytes(message, "utf8"))
    
    def do_POST( self ):
        
        if self.path=="/upload":
            self.send_response(200)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            
            content_length = int(self.headers['Content-Length'])
            self.post_data = (self.rfile.read(content_length)).decode()
            Control_Panel.ControlPanel1(self.post_data)

            
        elif self.path=="/upload2":
            self.send_response(200)
            self.send_header( 'Content-type', 'text/html' )
            self.end_headers()
            
            content_length = int(self.headers['Content-Length'])
            self.sensor_data = (self.rfile.read(content_length)).decode()
            Control_Panel.ControlPanel2(self.sensor_data)
##
##        else:
##            self.send_response(404)
##            self.send_header( 'Content-type', 'text/html' )
##            self.end_headers()
##            message = "Unknown Request"
##            self.wfile.write(bytes(message, "utf8"))

httpd = http.server.HTTPServer( ('', 80), Handler )

httpd.serve_forever()
