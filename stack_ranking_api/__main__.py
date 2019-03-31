#!/usr/bin/python3
# coding: utf8

from aiohttp import web
from routes import setup_routes
import threading
import config
import stackjob

def app():
    app = web.Application()
    setup_routes(app)
    web.run_app(app,host=config.IP_ADDRESS, port=config.PORT)

if __name__ == '__main__':
    thread = threading.Thread(target=stackjob.run_job)
    thread.start()
    app()
