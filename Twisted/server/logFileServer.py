__author__ = 'tuyou'
from twisted.internet.protocol import Factory
from twisted.internet import reactor
from twisted.protocols.basic import LineReceiver


class LoggingProtocol(LineReceiver):

    def lineReceived(self, line):
        self.factory.fp.write(line + '\n')


class LogfileFactory(Factory):

    protocol = LoggingProtocol

    def __init__(self, fileName):
        self.file = fileName

    def startFactory(self):
        self.fp = open(self.file, 'a')

    def stopFactory(self):
        self.fp.close()

reactor.listenTCP(10000, LogfileFactory("logFileServer.log"))
reactor.run()