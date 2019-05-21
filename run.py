from server import common
from gevent.pywsgi import WSGIServer

if __name__ == '__main__':
    http = WSGIServer(
        (
            common.app.config['HOST'], 
            common.app.config['PORT']
        ), 
        common.app.wsgi_app
    )
    http.serve_forever()
