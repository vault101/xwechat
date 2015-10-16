#!/usr/bin/env python
# encoding=utf-8
import json

from bottle import route, run, view, static_file, request

from crawler.wechat_crwaler import crawl


@route('/static/<tp>/<file_name>')
def route_static_file(tp, file_name):
    print tp, file_name
    return static_file(file_name, root='static/%s/' % tp)


@route('/')
@view('index')
def index():
    return {
        'title': '微信搜索器 － xlzd',
        'description': u'专栏作者；一个在80%情况下『理性、严谨、用数据说话』的技术宅。',
    }


@route('/search')
def search():
    request_params = request.GET.decode('utf-8')
    key = request_params.get("key")
    # print key, type(key)
    result = crawl(key)
    return json.dumps(result, ensure_ascii=False)


if __name__ == '__main__':
    PORT = 9132
    WORKERS = 2
    run(host='0.0.0.0', port=PORT, server='gunicorn', workers=WORKERS)
    # run(host='0.0.0.0', port=PORT)
