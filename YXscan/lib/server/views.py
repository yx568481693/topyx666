# -*- coding: utf-8 -*-
#import os,time
from gevent import monkey
from gevent.pywsgi import WSGIServer
from server.app import cmsserver
from flask import render_template, request, abort
#from server import CMSscan
from plugin.bruter import CMS_rec
from plugin.exp import CMS_exp
from plugin.read import tools
#app.config.from_object('config')
CMSscan = CMS_rec()
CMSexp = CMS_exp()

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
#        print "ssss"
        CMSscan.run()
        result = CMSscan.result()
        return render_template('scan.html', result=result)
    elif request.method == 'GET':
        return render_template('scan.html', )
#    return redirect(url_for('result.html))

#@cmsserver.route('/result/<>')
@cmsserver.route('/exp')
def exp():
    if request.method == 'POST':
        arg_ip = request.form.get('hosts', type=str, default=None)
        arg_thread = request.form.get('threads', type=int, default=None)
        arg_exp = request.form.get('exp', type=str, default=None)
        print arg_exp
        CMSexp.Int(arg_ip, arg_thread)
        CMSexp.readpoc(arg_exp)
        CMSexp.run()
        exp_result = CMSexp.result()
        return render_template('exp.html', tools=tools, result=exp_result)
    elif request.method == 'GET':
        return render_template('exp.html', tools=tools)
