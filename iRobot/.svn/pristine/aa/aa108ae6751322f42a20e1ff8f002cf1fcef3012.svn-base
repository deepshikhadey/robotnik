# Echo server program
#!flask/bin/python
import gzip
import random
import socket
import sys
import time
import collections

from flask import Flask, render_template
#app = Flask(__name__)
from app import app

host = ''                 # Symbolic name meaning the local host
port = 50000
backlog = 5
size = 1
serverSock = None
sock = None
client = None

robosignals = collections.namedtuple('robosignals', 'forward, back, left, right, stop, shutdown')._make(['f', 'b', 'l', 'r', 's', 'h'])

def connect_to_serial_host():
    """
    """

    global serverSock
    try:
        if serverSock:
            serverSock.close()
            print 'In connect: trying to sleep for 10 sec..'
            time.sleep(10)
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        serverSock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        serverSock.bind((host,port))
        serverSock.listen(backlog)
    except socket.error, (code,message):
        print "Could not open socket: " + message
        sys.exit(1)
    return serverSock

@app.route('/')
@app.route('/index')
def index():
  startup()
  return render_template('index.html')

#@app.route('/right')
#def right_in():
#    return 'Hello World'

@app.route('/left')
def left():
    """
    """
    global client
    #while True:
    try:
        print 'From left controller:', robosignals.left
        client.send(robosignals.left)
    except socket.error:
        print 'Connection was closed by remote host. Will just wait for it to come'\
              ' up again..'
        index()
    return render_template('index.html')


@app.route('/right')
def right():
    """
    """
    global client
    try:
        print 'From right controller:', robosignals.right
        client.send(robosignals.right)
    except socket.error:
        print 'Connection was closed by remote host. Will just wait for it to come'\
              ' up again..'
        index()
    return render_template('index.html')


@app.route('/up')
def forward():
    """
    """
    global client
    try:
        print 'From forward controller:', robosignals.forward
        client.send(robosignals.forward)
    except socket.error:
        print 'Connection was closed by remote host. Will just wait for it to come'\
              ' up again..'
        index()
    return render_template('index.html')


@app.route('/down')
def back():
    """
    """
    global client
    try:
        print 'From back controller:', robosignals.back
        client.send(robosignals.back)
    except socket.error:
        print 'Connection was closed by remote host. Will just wait for it to come'\
              ' up again..'
        index()
    return render_template('index.html')


@app.route('/stop')
def stop():
    """
    """
    global client
    try:
        print 'From stop controller:', robosignals.stop
        client.send(robosignals.stop)
    except socket.error:
        print 'Connection was closed by remote host. Will just wait for it to come'\
              ' up again..'
        index()
    return render_template('index.html')


@app.route('/index')
def shutdown():
    """ To make the robot go to a passive/safe mode once we are done playing
    """
    global client
    try:
        print 'From shutdown controller:', robosignals.shutdown
        client.send(robosignals.stop)
    except socket.error:
        print 'Connection was closed by remote host. Will just wait for it to come'\
              ' up again..'
        index()
    return render_template('index.html')


# main function that starts the server
def startup():
    """
    """
    global client
    sock = connect_to_serial_host()
    try:
        print 'waiting for client to connect..'
        if sock:
                client, address = sock.accept()
                """
                while True:
                    forward(client)
                    time.sleep(1)
                    left(client)
                    time.sleep(1)
                    right(client)
                    time.sleep(1)
                    back(client)
                    time.sleep(1)
                    stop(client)
                    time.sleep(1)
                time.sleep(10)
                shutdown(client)
                """
        else:
            time.sleep(10)
            shutdown()
    except KeyboardInterrupt, e:
        print '\nGot an interrupt. Terminating the cron job..'
        #break
        shutdown(client)
        sock.close()
        sys.exit()



if __name__=='__main__':
    app.run(debug = True)
    startup()
