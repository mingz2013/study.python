#!/usr/bin/env python3
#-*- coding: utf-8 -*-
##############################################
# Home  : http://netkiller.github.com
# Author: Neo <openunix@163.com>
##############################################

##############################################
from multiprocessing import Process
from multiprocessing import Pool
from html.parser import HTMLParser,HTMLParseError
import asyncore, asynchat, socket, threading, queue
import subprocess, os, sys, getopt, configparser, logging
import string, re
import random,time
import urllib.request, urllib.parse, http.client
#from urllib.parse import urlparse

queue = queue.Queue()

class MyHTMLParser(HTMLParser):
	urls 	= []
	def handle_starttag(self, tag, attrs):
		# Only parse the 'anchor' tag.
		if tag == "a":
			# Check the list of defined attributes.
			for name, value in attrs:
				# If href is defined, print it.
				if name == "href":
					#print name, "=", value
					if value and (value.find('javascript') == -1) and (value not in ('#')):
						self.urls.append(value)
	#def handle_endtag(self, tag):
		#print("Encountered  an end tag:", tag)
	#	pass
	#def handle_data(self, data):
		#print("Encountered   some data:", data)
	#	pass
	def gethref(self):
		return self.urls

class Spider():
	logfile = '/tmp/spider.log'
	isdebug = False
	depths = 0
	link	= []
	unlink	= []
	
	referer 	= ''
	useragent 	= 'Neo spider'
	domain		= r''
	baseurl		= r''
	
	skip	= []
	ignore	= []
	
	threadname = ''
	def __init__(self, threadname = None):
		logging.basicConfig(level=logging.NOTSET,
			format='%(asctime)s %(levelname)-8s %(message)s',
			datefmt='%Y-%m-%d %H:%M:%S',
			filename=self.logfile,
			filemode='a')
		self.logging = logging.getLogger()
		if threadname:
			self.threadname = '|'+threadname
	def setDebug(self,isdebug):
		self.isdebug = isdebug
		self.logging.debug('Enable Debug')
	def setDomain(self, tmp):
		if tmp:
			self.domain = tmp
	def setReferer(self,tmp):
		if tmp:
			self.referer = tmp
	def setUseragent(self,tmp):
		if tmp:
			self.useragent = tmp
	def setBaseUrl(self,tmp):
		if tmp:
			self.baseurl = tmp
	def ufilter(self,url):
		if (url not in self.link) :
			self.link.append(url)
		else:
			if url not in self.skip:
				self.skip.append(url)
				self.logging.warning('Skip ' + url)	
			return(None)
		
		if url[0:1] == '/':
			return(self.baseurl + url)
		elif url.find('http://') == -1:
			return(self.baseurl +'/'+ url)
		else:
			if url.find(self.domain) == -1:
				if url not in self.ignore:
					self.logging.warning('Ignore ' + url)
					self.ignore.append(url)
				return(None)

		return(url)

	def working(self, myurl):
		self.depths = self.depths + 1
		if self.depths > 256:
			return()
		#if self.isdebug:
		#	self.logging.debug('>>>' + str(self.depths))
		url = self.ufilter(myurl)
      			
		if url == None:
			return()
		else:
			self.link.append(myurl)
			if self.baseurl:
				urlparse = urllib.parse.urlparse(url)
				self.setBaseUrl(urlparse.scheme+ '://' + urlparse.netloc)
			#self.setDomain(urlparse.netloc)
			#print(urlparse)
			#uri.path
		   	#uri.params
		   	#uri.query
		   	#uri.fragment

		try:
			lines	= []
			parser = MyHTMLParser()
			#html = urllib.request.urlopen(myurl)
			#body = html.read()
			#html.close()
			req = urllib.request.Request(url)
			req.add_header('User-agent', self.useragent)
			req.add_header('Referer', self.referer)
			response = urllib.request.urlopen(req, timeout = 10)
			status 	= response.status
			reason 	= response.reason
			headers = response.info()
			
			log = str(status)+' '+reason+' '+myurl+ ' ('+ str(self.depths)+self.threadname+') '
			
			if self.isdebug:
				#print(response.geturl())
				print(log)
				#print(headers)
			if headers['Content-Type'] in ('text/html'):
				if status == 200:
					body 	= response.read()
					parser.feed(bytes.decode(body))
					lines = parser.gethref()
					self.logging.info(log)
				elif status == 302:
					self.unlink.append(myurl)
					self.logging.critical(log)
				else:
					self.logging.warning(log)

				response.close()
							
				if lines:
					self.referer = random.choice(lines)
					for line in lines:
						#result = re.match ('/http://"(.*)"/"(.*)"', line)
						self.working(line)
						self.depths = self.depths - 1
						#if self.isdebug:
						#	self.logging.debug('<<<' + str(self.depths))
			else:
				self.logging.warning(log + ' ' + headers['Content-Type'])
				response.close()
		except socket.timeout as e:
			self.logging.error(str(e) +' '+ myurl)			
		except urllib.error.URLError as e:
			if self.isdebug:
				print (str(e) +' '+myurl + ' - ' + url) 
			if (e.code == 404):
				self.unlink.append(myurl)
			else:
				print(e.code)
			self.logging.critical(str(e) +' '+ myurl)
		except urllib.error.HTTPError as e:
			self.logging.critical(str(e) +' '+ myurl)		
		except HTMLParseError as e:
			self.logging.error(str(e) +' '+ myurl)
			if self.isdebug:
				print (str(e) +' '+ myurl) 
		except UnicodeDecodeError as e:
			self.logging.critical(str(e) +' '+ myurl)
		except ValueError as e:
			if self.isdebug:
				print (str(e) +' '+ myurl) 			
		#else:
			#self.logging.error(myurl)
		#finally:
			#self.depths = self.depths - 1
			#pass

class ThreadSpider(threading.Thread):
	def __init__(self, queue):
		threading.Thread.__init__(self)
		self.queue = queue

		self.spider = Spider(str(self.name))
		self.spider.setDebug(True)
		
	def run(self):
		while True:
			#grabs host from queue
			host = self.queue.get()
			self.spider.setDomain(host)
			self.spider.working(host)

			#signals to queue job is done
			self.queue.task_done()

def Multithreading():
	workers	= 5
	hosts = ['http://www.example.com/','http://brand.example.com/','http://list.example.com/','http://item.example.com/']
	#spawn a pool of threads, and pass them queue instance 
	for i in range(workers):
		t = ThreadSpider(queue)
		t.setDaemon(True)
		t.start()

	#populate queue with data   
	for host in hosts:
		queue.put(host)

	#wait on the queue until everything has been processed     
	queue.join()

	#p = Pool(processes = 5)
	#p.map(test, [b'http://www.163.com/',b'http://www.sina.com/',b'http://www.qq.com/'])

def test(url):
	spider = Spider()
	spider.setDebug(True)
	spider.working(url)
	print(url)

def daemon(isdaemon):
	if isdaemon :
		pid = os.fork()
		if pid > 0:
			sys.exit(0)
	
def main():
	daemon(isdaemon = False)

	myurl 		= r'http://www.example.com'
	#myurl 		= r'http://www.example.com/mobile.html'
	try:
		start = time.time()
		spider = Spider()
		spider.setDebug(True)
		spider.setDomain('www.example.com')
		spider.setBaseUrl(myurl)
		spider.working(myurl)
		print("Elapsed Time: %s" % (time.time() - start))
	except RuntimeError as e:
		print(e)

if __name__ == '__main__':
	try:
		main()
		#Multithreading()
	except KeyboardInterrupt:
		print ("Crtl+C Pressed. Shutting down.")

		
