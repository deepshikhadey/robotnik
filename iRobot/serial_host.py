# Echo client program
import collections
import logging
import os
import pyrobot
import socket
import sys
import time

from os import stat
from os.path import abspath
from stat import ST_SIZE

# Socket values
HOST = 'localhost'    # The remote host
PORT = 50000          # The same port as used by the server
size = 1
count = 0

# Robot values
robosignals = collections.namedtuple('robosignals', 'forward, back, left, right, stop, shutdown')._make(['f', 'b', 'l', 'r', 's', 'h'])
velocity = 100
roboconnected = False
portname = None

# main function to start the client
def main():
    """
    """
    if roboconnected:
        # Start robot serial session
        # TODO: Put robot in SAFE mode so it doesn't hurt itself?
        robot = pyrobot.Create(portname)
        robot.sci.start()
        robot.Control()
        robot.LedControl([1,1,1])
        time.sleep(0.2)
        robot.LedControl([0,0,0])

    # Set up socket to talk to controller
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
    sock.send('Hello, world')

    while sock:
        try:
            robosignal = sock.recv(size)
            print str(robosignal)
            if roboconnected:
                if robosignal == robosignals.forward:
                    robot.DriveStraight(velocity)
                elif robosignal == robosignals.back:
                    robot.DriveStraight(-velocity)
                elif robosignal == robosignals.left:
                    robot.TurnInPlace(velocity, 'ccw')
                elif robosignal == robosignals.right:
                    robot.TurnInPlace(velocity, 'cw')
                elif robosignal == robosignals.stop:
                    robot.Stop()
                elif robosignal == robosignals.shutdown:
                    robot.SoftReset()
                else:
                    raise Exception('Unrecognized robosignal: ', robosignal)

        except KeyboardInterrupt, e:
            print 'Got an interrupt'
            raise
    sock.close()


if __name__=='__main__':
    if len(sys.argv) > 1:
        portname = sys.argv[1]
        roboconnected = True
        main()
    else:
        main()
