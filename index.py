import bae.core.wsgi import WSGIApplication
def app(environ, start_response): 
    status = '200 OK' 
    headers = [('Content-type', 'text/html')] 
    body = ['hello guys\n\n'] 
    start_response(status, headers) 
    return body
application = WSGIApplication(app)
