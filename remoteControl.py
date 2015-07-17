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

from daemon import Daemon

class RemoteControl(SocketServer.ThreadingTCPServer, Daemon):
	
	PORT = 1337

	def __init__(self, port=1337):
		Daemon.__init__(self, '/var/run/remoteControl.pid', stdout='/dev/stdout', stderr='/dev/stderr')#, stderr = '/var/log/remoteControl.errlog')
		self.PORT = port
		self.log('Remote Control server started at port %d' % self.PORT)

	def run(self):
		# handle Ctrl + C, if running in no-daemon mode
		signal.signal(signal.SIGINT, self.signal_handler)
		# handle termination signal, if running in daemon mode
		signal.signal(signal.SIGTERM, self.signal_handler)

		try:
			SocketServer.ThreadingTCPServer.__init__(self, ('0.0.0.0', self.PORT), RCHandler)
		except:
			self.log('Unable to bind port %d' % self.PORT)
			exit(1)

		self.serve_forever()

	def log(self, msg):
		sys.stderr.write(time.asctime(time.localtime(time.time())) + ': ')
		sys.stderr.write(msg.rstrip() + '\n')

	def signal_handler(self, signum, frame):
		self.log('Remote Control server stopped')
		sys.exit(0)


class RCHandler(SocketServer.BaseRequestHandler):

	def setup(self):
		pass

	def handle(self):
		while True:
			recv = self.request.recv(1024)

			if len(recv) < 1:
				break

			self.server.log(recv)

			if recv == 'quit':
				break

			self.request.send(recv)


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
