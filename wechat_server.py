from bottle import route, run, template, view, static_file


@route('/static/<file_name>')
def route_static_file(file_name):
	return static_file(file_name, root='static/')

@route('/')
@view('index')
def index():
    return {}


@route('/search/<key>')
def search(key):
	return key


if __name__ == '__main__':
	PORT = 9132
	WORKERS = 2
	run(host='0.0.0.0', port=PORT, server='gunicorn', workers=WORKERS)