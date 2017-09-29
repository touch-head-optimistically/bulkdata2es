#encoding=UTF-8
#!/user/bin/python

import json,time
import threading,random
import pycurl
import sys


class mythread01(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
            #value[2]=value[2].replace('-','')
            #value[2]=value[2].replace(':','')
            global number
            num=random.randint(1, 100)
            bodydata='''{ "create" :{} }
            {"f11" : "%d"\n}
            '''%number
            py=pycurl.Curl()
            body=bodydata
            print body
            #body=json.dumps(body, sort_keys=True)
            #body2=json.dumps(bodydata2, sort_keys=True)
            #print body+body2
            #print body
            #url=['http://192.168.xx.xx:xx/001/001/_bulk']
            url = [ip + ":" + port + "/001/001/_bulk"]
            py.setopt(pycurl.URL,random.choice(url))
            py.setopt(pycurl.POSTFIELDS, body)
            py.setopt(pycurl.CONNECTTIMEOUT,9600)
            py.setopt(pycurl.WRITEFUNCTION,lambda x: None)
            py.perform()
            response_code = py.getinfo(pycurl.RESPONSE_CODE)
            print response_code

if __name__=='__main__':
    global start, number, ip, port

    ip = sys.argv[1]
    port = sys.argv[2]
    threads=[]

    number=0
    for x in range(10):
        x=mythread01()
        threads.append(x)
    start = time.time()
    for y in threads:
        y.start()
    for j in threads:
        j.join()
    end=time.time()
    print 'usetime=%r'%(end-start)









































