#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

async def index(request):
	return web.Response(body='<h1>Sunmonday</h1>', content_type='text/html')

async def hello(requset):
	await asyncio.sleep(0.5)
	text = '<h1>hello, %s!</h1>' % requset.match_info['name']
	return web.Response(body=text.encode('utf-8'), content_type='tx')
	
app = web.Application()
app.add_routes([web.get('/', index), web.get('/hello/{name}', hello)])
web.run_app(app, host='127.0.0.1', port=8000)
logging.info('server started at http://127.0.0.1:8000...')
