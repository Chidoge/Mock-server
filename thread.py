import thread
from threading import Thread,Event
import urllib3
import json
import time
import random


class MyThread(Thread):

    def __init__(self):
        Thread.__init__(self)
        self._stop_event = Event()


    def run(self):

        while not self._stop_event.wait(1):

            ts = time.time()
            encoded_body = json.dumps({
                "ID": random.randint(0,1),
                "location" : {
                    "x" : random.uniform(0, 2500),
                    "y" : random.uniform(0, 2500)
                },
                "time": ts
            })
            http = urllib3.PoolManager()
            r = http.request('POST', 'http://localhost:3000/postNewData',headers={'Content-Type': 'application/json'},body=encoded_body)



    def stop(self):

    	self._stop_event.set()

