__author__ = 'tuyou'
from twisted.protocols.basic import LineReceiver
from twisted.internet import protocol, reactor

class Answer(LineReceiver):

    answers = {'How are you?': 'Fine', None: "I don't know what you mean"}

    def lineReceived(self, line):
        if self.answers.has_key(line):
            self.sendLine(self.answers[line])
        else:
            self.sendLine(self.answers[None])

class AnswerFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Answer()

reactor.listenTCP(10000, AnswerFactory())
reactor.run()