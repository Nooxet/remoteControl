#!/usr/bin/python

"""
A program for controlling desktop applications
over the TCP protocol, for easy access from
phones, tablets or even a website.

2015-07-16
Noxet

"""

import sys
import time
import syslog
import signal
import SocketServer
import json
import logging

from daemon import Daemon
from mediaFinder import MediaFinder

class RemoteControl(SocketServer.ThreadingTCPServer, Daemon):

	def __init__(self, port=1337):
		Daemon.__init__(self, '/var/run/remoteControl.pid', stdout='/dev/stdout', stderr='/dev/stderr')#, stderr = '/var/log/remoteControl.errlog')
		self.PORT = port

		logging.basicConfig(format='%(levelname)s: %(asctime)s - %(message)s', 
			datefmt='%d/%m/%Y %I:%M:%S', level=logging.DEBUG)
		logging.info('Remote Control server started at port %d' % self.PORT)

	def run(self):
		# handle Ctrl + C, if running in no-daemon mode
		signal.signal(signal.SIGINT, self.signal_handler)
		# handle termination signal, if running in daemon mode
		signal.signal(signal.SIGTERM, self.signal_handler)

		try:
			SocketServer.ThreadingTCPServer.__init__(self, ('0.0.0.0', self.PORT), RCHandler)
		except:
			logging.error('Unable to bind port %d' % self.PORT)
			exit(1)

		self.serve_forever()

	def signal_handler(self, signum, frame):
		logging.info('Remote Control server stopped')
		sys.exit(0)


class RCHandler(SocketServer.BaseRequestHandler):

	def setup(self):
		pass

	def handle(self):
		raw = self.request.recv(1024)
		if not raw:
			return

		# clean all whitespace
		recv = raw.strip()

		# do some logging
		logging.debug("(%s) sent: %s" % (self.client_address, recv))
		
		# try parsing data as JSON
		try:
			data = json.loads(recv)
		except ValueError:
			logging.error('JSON parsing error: %s' % recv)
			return
		except:
			logging.error('Someting strange happened...')
			return



	def parseJSON(self, data):
		pass


if __name__ == '__main__':
	rc = RemoteControl()

	if len(sys.argv) == 2 or len(sys.argv) == 3:
		if sys.argv[1] == 'start':
			rc.start()
		elif sys.argv[1] == 'stop':
			rc.stop()
		elif sys.argv[1] == 'restart':
			rc.restart()
		elif sys.argv[1] == 'nod': # no-daemon mode
			rc.run()
		else:
			print 'Unknown command'
			sys.exit(2) # command line error		
		sys.exit(0)
	else:
		print 'Usage: %s start|stop|restart|nod' % sys.argv[0]
		sys.exit(2)
