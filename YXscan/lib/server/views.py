# -*- coding: utf-8 -*-
#import os,time
from gevent import monkey
from gevent.pywsgi import WSGIServer
from server.app import cmsserver
from flask import render_template, request, abort
#from server import CMSscan
from plugin.bruter import CMS_rec

#app.config.from_object('config')
CMSscan = CMS_rec()

@cmsserver.route('/')
@cmsserver.route('/index')
def index():

    return render_template('index.html')

@cmsserver.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        arg_ip = request.form.get('hosts', type=str, default=None)
        arg_thread = request.form.get('thread', type=int, default=None)
        print arg_ip
        CMSscan.Int(arg_ip,arg_thread)
        print "ssss"
        CMSscan.run()
        result = CMSscan.result()
    elif request.method == 'GET':
        result = 1
    return render_template('scan.html', result=result)
#    return redirect(url_for('result.html))

#@cmsserver.route('/result/<>')
@cmsserver.route('/exp')
def exp():
    return render_template('show_entries.html')
