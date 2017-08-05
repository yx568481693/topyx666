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
        scan_ip = request.form.get('hosts', type=str, default=None)
        scan_thread = request.form.get('thread', type=int, default=None)
        CMSscan.Int(scan_ip,scan_thread)
#        print "ssss"
        CMSscan.run()
        result = CMSscan.result()
        return render_template('scan.html', result=result)
    elif request.method == 'GET':
        return render_template('scan.html', )
#    return redirect(url_for('result.html))

#@cmsserver.route('/result/<>')
@cmsserver.route('/exp', methods=['GET', 'POST'])
def exp():
    if request.method == 'POST':
        exp_ip = request.form.get('exp_hosts', type=str, default=None)
        exp_thread = request.form.get('exp_threads', type=int, default=None)
        exp_exp = request.form.get('exp', type=str, default=None)
        print exp_thread
        CMSexp.Int(exp_ip, exp_thread)
        CMSexp.run(exp_exp)
        exp_result = CMSexp.result()
        return render_template('exp.html', tools=tools, result=exp_result)
    elif request.method == 'GET':
        return render_template('exp.html', tools=tools)
