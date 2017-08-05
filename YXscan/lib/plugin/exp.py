#	-*-	coding:	utf-8	-*-
#from read import list1
import urllib2
import requests
import threading
import Queue

class CMS_exp():
    def __init__(self):
        self.hosts = None
        self.threads = None
        self.Threadlist = []
        self.queue = Queue.Queue()
        self.scan_result = []
        self.status = {}

    def Int(self, hosts, threads):
        self.hosts = hosts
        self.threads = threads

    def load(self, urlp):
        if self.hosts.endswith('/'):
            self.hosts = self.hosts[:-1]
        if self.hosts.startswith('http://') or self.hosts.startswith('https://'):
            pass
        else:
            self.hosts = 'http://'+self.hosts

        path = '/home/nanke/桌面/YXscan/exp/' + urlp
        f = open(path)
        poc = f.readlines()
        for line in poc:
            if len(line.strip())==0 or line.startswith('#'):
                pass
            else:
                self.queue.put(line.strip())
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
                html = requests.get(self.hosts+poc,timeout=5)
            except:
                continue
            if html.status_code == 200:
                print "Result:"
                print self.hosts + poc
                f = self.hosts + poc
                self.scan_result.append(f)

    def result(self):
        if self.hosts is not None and self.threads is not None:
            return self.scan_result

    def run(self, urlpath):
        if type(self.status) == dict:
            urlp = urlpath
            self.load(urlp)

    def status(self):
        return {"hosts": self.hosts, "threads": self.threads}

#if __name__ == '__main__':
