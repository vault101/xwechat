from bottle import route, run, template

@route('/')
def index():
    return "hello, world."


if __name__ == '__main__':
	PORT = 9132
	WORKERS = 2
	run(host='0.0.0.0', port=PORT, server='gunicorn', workers=WORKERS)