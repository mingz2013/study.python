__author__ = 'tuyou'
from twisted.internet.protocol import Protocol
from twisted.internet import protocol, reactor

class Echo(Protocol):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.numProtocols = self.factory.numProtocols + 1
        self.transport.write("Welcome! there are currently %d open connections.\n" % (self.factory.numProtocols))

    def connectionLost(self, reason):
        self.factory.numProtocols = self.factory.numProtocols - 1

    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def __init__(self):
        self.numProtocols = 0
    def buildProtocol(self, addr):
        return Echo(self)

reactor.listenTCP(1236, EchoFactory())
reactor.run()
