#!/usr/bin/python3


import sys
import Ice
Ice.loadSlice('Printer.ice')
import argparse
import Example


class Client(Ice.Application):
    def run(self, argv):
        parser = argparse.ArgumentParser(description='Client for Ice Printer')
        parser.add_argument('--proxy', help='proxy to use')
        parser.add_argument('--operation', choices=['add', 'multiply'], help='operation to perform')
        parser.add_argument('--num1', type=int, help='first number')
        parser.add_argument('--num2', type=int, help='second number')
        args = parser.parse_args()

        proxy = self.communicator().stringToProxy(argv[2])
        printer = Example.mathPrx.checkedCast(proxy)

        if not printer:
            raise RuntimeError('Invalid proxy')

        if args.operation == 'add':
            result = printer.add(args.num1, args.num2)
        elif args.operation == 'multiply':
            result = printer.multiply(args.num1, args.num2)

        print(f'Result: {result}')

        return 0


sys.exit(Client().main(sys.argv))

