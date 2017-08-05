#	-*-	coding:	utf-8	-*-
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import threading
import urllib2
import Queue
import requests
import argparse

class CMS_rec():
    def __init__(self):
        self.hosts = None
        self.threads = None
        #self.scan_result = None
        self.Threadlist = []
        self.queue = Queue.Queue()
        self.flag = 0
        self.scan_result = {}
        self.status = {}


    def Int(self, hosts, threads):
        self.hosts = hosts
        self.threads = threads


    def load(self):
        if self.hosts.endswith('/'):
            self.hosts = self.hosts[:-1]
        if self.hosts.startswith('http://') or self.hosts.startswith('https://'):
            pass
        else:
            self.hosts = 'http://'+self.hosts

        f = open('/home/nanke/桌面/YXscan/dic/cmsdict.txt')
        cms = f.readlines()
        for line in cms:
            if len(line.strip())==0 or line.startswith('#'):
                pass
            else:
                self.queue.put(line.strip())
        self.start_thread()

    def start_thread(self):
        #run it ok
        for i in range(self.threads):
            t = threading.Thread(target=self.start_scan)
            t.start()
            self.Threadlist.append(t)
            #print i
        for T in self.Threadlist:
            T.join()

    def start_scan(self):
        #run it ok
        while True:
            if self.flag == 1:
                break
            #queue.get([block[, timeout]]), there is not [block], [timeout] can't exist alone
            try:
                data = self.queue.get(block=True,timeout=1)
            except:
                break
            url,pattern,cmsname = data.split('------')
            try:
                print self.hosts+url
                html = requests.get(self.hosts + url,timeout = 5)
            except:
                continue
            if pattern.upper() in html.text.upper() and html.status_code == 200:
                #print "You know"
                #print {'Scan Result':cmsname.strip('\n').strip('\r'),'matched url':url,'matching rule':pattern.decode('utf-8')}
                self.scan_result = {'Scan Result':cmsname.strip('\n').strip('\r'),'matched url':self.hosts+url,'matching rule':pattern}
                self.flag = 1

    def result(self):
        if self.hosts is not None and self.threads is not None:
            return self.scan_result

    def run(self):
        if type(self.status) == dict:
            #self.hosts = self.status.get('hosts',None)
            #self.threads = self.status.get('threads',None)
            self.load()

    def status(self):
        return {"hosts": self.hosts, "threads": self.threads}

#if __name__ == '__main__':
#    parser = argparse.ArgumentParser()
#    parser.add_argument('scanSite', help="The website to be scanned", type=str)
#    parser.add_argument('-t', '--thread', dest="threadNum", help="Number of threads running the program", type=int, default=60)
#    args = parser.parse_args()
#    scan = CMS_rec(args.scanSite, args.threadNum)
#    scan.run()
