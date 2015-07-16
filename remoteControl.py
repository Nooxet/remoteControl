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
import SocketServer

from daemon import Daemon

class remoteControl(SocketServer.ThreadingTCPServer, Daemon):
	
	PORT = 1337

	def __init__(self, port=1337):
		Daemon.__init__(self, '/var/run/remoteControl.pid', stderr = '/var/log/remoteControl.errlog')
		self.PORT = port
		self.log('Remote Control server started at port %d' % self.PORT)

	def run(self):
		try:
			SocketServer.ThreadingTCPServer.__init__(self, ('0.0.0.0', self.PORT), RCHandler)
		except:
			self.log('Unable to bind port %d' % self.PORT)
			exit(1)

		self.serve_forever()

	def log(self, msg):
		sys.stderr.write(time.asctime(time.localtime(time.time())) + ': ')
		sys.stderr.write(msg.rstrip() + '\n')

if __name__ == '__main__':
	rc = remoteControl()
	rc.start()
