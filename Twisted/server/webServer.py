from twisted.web import server, resource
from twisted.internet import reactor
# Twisted includes an event-driven web server. Here's a sample web application; notice how the resource object persists in memory, rather than being recreated on each request:
class HelloResource(resource.Resource):
    isLeaf = True
    numberRequests = 0

    def render(self, request):
        self.numberRequests += 1
        request.setHeader("content-type", "text/plain")
        return "I an request #" + str(self.numberRequests) + "\n"

reactor.listenTCP(8080, server.Site(HelloResource()))
reactor.run()