#_*_ coding:utf-8 _*_

'''
为 你的处理目的而写一个自定义的protocol是很容易的。
模块twisted.protocols.basic中包含了几个有用的已存在的 protocol，
其中的LineReceiver执行dataReceived并在接受到了一个完整的行时调用事件处理器lineReceived。
如 果当你在接受数据时除了使用lineReceived,还要做些别的，那么你可以使用LineReceiver定义的名为rawDataReceived 事件处理器。
下面是一使用LineReceiver的服务器例子：
'''

from twisted.internet import reactor
from twisted.internet.prtocol import Factory
from twisted.prtocols.basic import LineReceiver

class SimpleLogger(LineReceiver):
	def connectionMade(self):
		print 'Got connection from', self.transport.client
	def connectionLost(self, reason):
		print self.transport.client, "disconnected"
	def lineReceived(self, line):
		print line

factory = Factory()
factory.prtocol = SimpleLogger

reactor.listenTCP(1234, factory)
reactor.run()