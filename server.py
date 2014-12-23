#!/usr/bin/python -tt
from werkzeug.wrappers import Response, Request
from werkzeug.serving import run_simple
import posixpath, urllib, os, mimetypes, json, sqlite3

def application(environ, start_response):
	request = Request(environ)
	path = translate_path(request.path)
	print path
	if os.path.isdir(path) and os.path.exists(os.path.join(path,"index.html")):
		path = os.path.join(path,"index.html")
		f = open(path,'rb')
	elif os.path.exists(path):
		f = open(path,'rb')
	else:	
		response = Response("404 not found")
		response.status_code = 404
		return response(environ, start_response)
	response = Response(f.read(), mimetype=mimetypes.guess_type(path)[0])
	return response(environ, start_response)

def translate_path(path):
	# abandon query parameters
	path = path.split('?',1)[0]
	path = path.split('#',1)[0]
	path = posixpath.normpath(urllib.unquote(path))
	words = path.split('/')
	words = filter(None, words)
	path = os.path.join(os.getcwd(),"www")
	for word in words:
		drive, word = os.path.splitdrive(word)
		head, word = os.path.split(word)
		if word in (os.curdir, os.pardir): continue
		path = os.path.join(path, word)
	return path

if __name__ == '__main__':
	run_simple('0.0.0.0', 80, application, use_reloader=True)
