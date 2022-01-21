from wsgiref.simple_server import make_server

import json
import sys
import os
import shutil

sys.path.insert(1, os.path.dirname(shutil.which('xtract')))
import edirect

def app(environ, start_response):
    status = '200 OK'
    headers = [
                ('Content-type', 'application/json; charset=utf-8'),
                ('Access-Control-Allow-Origin', '*'),
              ]
    start_response(status, headers)

    wsgi_input = environ["wsgi.input"]
    # print(input)

    content_length = int(environ.get('CONTENT_LENGTH', 0))
    query = json.loads(wsgi_input.read(content_length))["query"]
    # print(query)
    
    try:
        res = edirect.execute(query)
    except Exception as e:
        res = e

    return [json.dumps({'message':res}).encode("utf-8")]

with make_server('', 3000, app) as httpd:
    print("Serving on port 3000...")
    httpd.serve_forever()
