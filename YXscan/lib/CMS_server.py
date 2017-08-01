# -*- coding: utf-8 -*-
from server.app import cmsserver
from gevent import monkey
from gevent.wsgi import WSGIServer

if __name__ == "__main__":
    #csfserver.run(host='0.0.0.0',debug=True)
    http_server = WSGIServer(('', 5000), cmsserver)
    http_server.serve_forever()
