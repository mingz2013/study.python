# _*_ coding:utf-8 _*_
'''
from twisted.internet.protocol import protocol
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet import reactor

class Echo(protocol):
	def dataReceived(self, data):
		self.transport.write(data)

class QOTD(protocol):
	def connectionMade(self):
		self.transport.write("An apple a day keeps the doctor away\r\n")
		self.transport.loseConnection()


class Echo2(protocol):
	def __init__(self, factory):
		self.factory = factory

	def connectionMade(self):
		self.factory.numProtocols = self.factory.numProtocols + 1
		self.transport.write("Welcome! There are currently %d open connections.\n" % (self.factory.numProtocols))

	def connectionLost(self, reason):
		self.factory.numProtocols = self.factory.numProtocols - 1

	def dataReceived(self, data):
		self.transport.write(data)
		
class QOTDFactory(Factory):
	def buildProtocol(self, addr):
		reason QOTD()

endpoint = TCP4ServerEndpoint(reactor, 8007)
endpoint.listen(QOTDFactory())
reactor.run()
'''

''''''''''''''''''''''''''''''''''''''''''
from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory
'''
Twisted使用了更多的基于事件的方式。
要写一个基本的服务器，你要实现事件处理 器，它处理诸如一个新的客户端连接、新的数据到达和客户端连接中断等情况。
在Twisted中,你的事件处理器定义在一个protocol中；
你也需要一 个factory,当一个新的连接到达时它能够构造这个protocol对象，但是如果你仅仅想创建一个自定义的Protocol类的实例的话，
你可以使 用来自Twisted的factory，Factory类在模块twisted.internet.protocol中。
当你写你的protocol时， 使用twisted.internet.protocol模块中的Protocol作为你的父类。
当你得到一个连接时，事件处理器 connectionMade被调用；当你丢失了一个连接时，connectionLost被调用。
从客户端接受数据使用处理器 dataReceived。
但是你不能使用事件处理策略向客户端发送数据；要向客户端发送数据，你可以使用self.transport，它有一个 write方法。
它也有一个client属性，其中包含了客户端的地址(主机名和端口)。

下面这个例子是一个Twisted版的服务器。 
其中实例化了Factory并设置了它的protocol属性以便它知道使用哪个protocol与客户端通信(这就是所谓的你的自定义 protocol)。
然后你使用factory开始监听指定的端口，factory通过实例化的protocol对象处理连接。
监听使用reactor模 块中的listenTCP函数。最后，你通过调用reactor模块中的run函数来开始服务器。
'''
# 定义Protocol类
class SimpleLogger(Protocol):
	def connectionMade(self):
		print 'Got connection from', self.transport.client
	def connectionLost(self, reason):
		print self.transport.client, "disconnected"
	def dataReceived(self, data):
		print data

# 实例化Factory
factory = Factory()

#设置factocy的protocol属性 以便它知道使用哪个protocol与客户端通信(这就是所谓的你的自定义protocol)
factory.protocol = SimpleLogger

#监听指定的端口
reactor.listenTCP(1234, factory)
# 开始运行主程序
reactor.run()



		
		