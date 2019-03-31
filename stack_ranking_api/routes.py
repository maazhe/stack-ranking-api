#!/usr/bin/python3
# coding: utf8

from aiohttp import web
import stackserver

def setup_routes(app):
    app.router.add_get('/monthly', stackserver.get_ranking_monthly)
    app.router.add_get('/overall', stackserver.get_ranking_overall)
    # app.router.add_get('/weekly', stackserver.get_ranking_weekly)
    app.router.add_get('/json', stackserver.get_users_json)
    app.router.add_get('/' , stackserver.get_home)

    # other static
    app.router.add_static('/static/', path='./static/', name='static')
    app.router.add_static('/templates/', path='./templates/', name='templates')