__author__ = 'tuyou'
from twisted.internet import reactor
from twisted.internet.protocol import Protocol
# from twisted.internet.endpoints import TCP4ClientEndpoint, connectProtocol
from twisted.internet.protocol import ClientCreator

class Greeter(Protocol):
    def sendMessage(self, msg):
        self.transport.write("MESSAGE %s\n" % msg)

def gotProtocol(p):
    p.sendMessage("Hello")
    reactor.callLater(1, p.sendMessage, "This is sent in a second")
    reactor.callLater(2, p.transport.loseConnection)


creator = ClientCreator(reactor, Greeter)
d = creator.connectTCP("localhost", 1234)
d.addCallback(gotProtocol)
reactor.run()