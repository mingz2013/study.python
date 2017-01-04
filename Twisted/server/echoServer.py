#_*_ coding:utf-8 _*_
#Twisted makes it easy to implement custom network applications. Here's a TCP server that echoes back everything that's written to it:
from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        print data;
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(1234, EchoFactory())
reactor.run()