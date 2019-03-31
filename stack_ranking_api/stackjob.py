#!/usr/bin/python3
# coding: utf8

import threading
import time
import requests
import json
import config

def get_user_dict(so_user):
    return {
            'reputation_change_year': so_user['reputation_change_year'],
            'reputation_change_quarter': so_user['reputation_change_quarter'],
            'reputation_change_month': so_user['reputation_change_month'],
            'reputation_change_week': so_user['reputation_change_week'],
            'reputation_change_day': so_user['reputation_change_day'],
            'reputation': so_user['reputation'],
            'link': so_user['link'],
            'profile_image': so_user['profile_image'],
            'display_name': so_user['display_name']
    }

def get_users_data():
    results = []
    for user in config.USERS:
        res = requests.get('{0}{1}?site=stackoverflow'.format(config.SO_API_URL, user['id']))
        result = json.loads(res.text)

        so_user = result.get('items', [])[0]
        if so_user:        
            results.append(get_user_dict(so_user))
        
    config.SO_USERS = results
    

def run_job():
    
    # run first time
    get_users_data()
    
    # 600 seconds / 10 minutes
    WAIT_TIME = 600
    
    ticker = threading.Event()
    while not ticker.wait(WAIT_TIME):
        get_users_data()
