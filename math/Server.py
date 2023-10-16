#!/usr/bin/python3 -u

import sys
import Ice

Ice.loadSlice('Printer.ice')
import Example


class PrinterI(Example.math):
    def add(self, a, b, current=None):
        return print(a + b)
    def multiply(self, a, b, current=None):
        return a*b


class Server(Ice.Application):
    def run(self, argv):
        broker = self.communicator()
        servant = PrinterI()

        adapter = broker.createObjectAdapter("PrinterAdapter")
        proxy = adapter.add(servant, broker.stringToIdentity("printer1"))

        print(proxy, flush=True)

        adapter.activate()
        self.shutdownOnInterrupt()
        broker.waitForShutdown()

        return 0


server = Server()
sys.exit(server.main(sys.argv))
