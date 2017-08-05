#	-*-	coding:	utf-8	-*-
#from read import list1
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2
import requests
import threading
import Queue

class CMS_exp():
    def __init__(self):
        self.hosts = None
        self.threads = None
        self.list1 =[]
        self.Threadlist = []
        self.queue = Queue.Queue()
        self.result = []
        self.status = {}

    def readpoc(self, urlpath):
        path = '/home/nanke/桌面/YXscan/exp/' + urlpath
        with open(path) as f:
            poc = f.readline()
            while poc:
                self.list1.append(poc)
                poc = f.readline()

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

        while self.list1:
            line = self.list1.pop()
            self.queue.put(self.list1.pop())
        self.start_thread()

    def start_thread(self):
        for i in range(self.threads):
            t = threading.Thread(target=self.start_scan)
            t.start()
            self.Threadlist.append(t)
            #print i
        for T in self.Threadlist:
            T.join()

    def start_scan(self):
        while True:
            try:
                poc = self.queue.get(block=True,timeout=1)
            except:
                break
            try:
                html = requests.get(self.hosts+url,timeout=5)
            except:
                continue
            if html.status_code == 200:
                print "Result:"
                print self.hosts + poc
                f = self.host + poc
                self.result.append(f)

    def result(self):
        if self.hosts is not None and self.threads is not None:
            return self.scan_result

    def run(self):
        if type(self.status) == dict:
            self.load()

    def ststus(slef):
        return {"hosts": self.hosts, "threads": self.threads}

#if __name__ == '__main__':
