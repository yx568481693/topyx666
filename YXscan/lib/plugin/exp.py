from read import list1
import urllib2
import requests
import threading
import Queue

class CMS_exp():
    def __init__():
        self.hosts = scanSite
        self.threads = threadNum
        self.queue = Queue.Queue()
        self.flag = 0
        self.result = {}

    def load(self):
        if self.hosts.endswith('/'):
            self.hosts = self.hosts[:-1]
        if self.hosts.startswith('http://') or self.hosts.startswith('https://'):
            pass
        else:
            self.hosts = 'http://'+self.hosts

        while list1:
            line = list1.pop()
            self.queue.put(list1.pop())
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
            if self.flag = 0
                break
        try:
            poc = self.queue.get(block=True,timeout=1)
        except:
            break
        try:
            html = requests.get(self.hosts+url,timeout=5)
        except:
            continue
        if html.status_code = 200:
            print "Result:"
            print self.hosts+poc
            self.flag = 1

    def result(self):
        if self.hosts is not None and self.threads is not None:
            return self.scan_result

    def run(self):
        if type(self.status) == dict:
        self.load()

    def ststus(slef):
        return {"hosts": self.hosts, "threads": self.threads}

#if __name__ == '__main__':
