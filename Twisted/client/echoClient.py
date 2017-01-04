__author__ = 'tuyou'
from twisted.internet.protocol import Protocol, ClientFactory
from sys import stdout
from twisted.internet import reactor

class Echo(Protocol):
    def dataReceived(self, data):
        stdout.write(data)

class EchoClientFactory(ClientFactory):
    def startedConnecting(self, connector):
        print 'Started to connect.'

    def buildProtocol(self, addr):
        print 'Connected.'
        return Echo()

    def clientConnectionLost(self, connector, reason):
        print 'Lost connection.  Reason:', reason
        connector.connect()
        '''
        Often, the connection of a client will be lost unintentionally due to network problems.
        One way to reconnect after a disconnection would be to call connector.connect()
        when the connection is lost:
        '''

    def clientConnectionFailed(self, connector, reason):
        print 'Connection failed. Reason:', reason


reactor.connectTCP("localhost", 1234, EchoClientFactory())
reactor.run()