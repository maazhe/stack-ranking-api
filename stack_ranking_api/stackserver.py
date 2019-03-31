#!/usr/bin/python3
# coding: utf8

from jinja2 import Environment, FileSystemLoader
from aiohttp import web
import config

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

def get_data_dict(period):
    return {
        'company_name': config.COMPANY_NAME,
        'period': period,
        'users' : config.SO_USERS
    }

def get_ranking_overall(request):
    template = env.get_template('ranking.html')
    data = get_data_dict('overall')
    page = template.render(data=data)
    return web.Response(text=page, content_type='text/html')

def get_ranking_monthly(request):
    template = env.get_template('ranking.html')
    data = get_data_dict('monthly')
    page = template.render(data=data)
    return web.Response(text=page, content_type='text/html')

def get_home(request):
    template = env.get_template('home.html')
    page = template.render(company_name=config.COMPANY_NAME)
    return web.Response(text=page, content_type='text/html')

def get_users_json(request):
    return web.json_response(config.SO_USERS)
