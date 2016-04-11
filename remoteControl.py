#!/usr/bin/python

"""
A program for controlling desktop applications
over the TCP protocol, for easy access from
phones, tablets or even a website.

2015-07-16
Noxet

"""

from __future__ import print_function
from __future__ import unicode_literals

import sys
import time
import syslog
import signal
#import SocketServer as sserver
import socketserver as sserver
import json
import logging

from mediaFinder import MediaFinder

class RemoteControl(sserver.ThreadingTCPServer):

	def __init__(self, port=1337):
		self.PORT = port
		self.mediafinder = MediaFinder('/home/noxet/Videos')

		logging.basicConfig(format='%(levelname)s: %(asctime)s - %(message)s', 
			datefmt='%d/%m/%Y %I:%M:%S', level=logging.DEBUG)
		logging.info('Remote Control server started at port %d' % self.PORT)

	def run(self):
		# handle Ctrl + C, if running in no-daemon mode
		signal.signal(signal.SIGINT, self.signal_handler)
		# handle termination signal, if running in daemon mode
		signal.signal(signal.SIGTERM, self.signal_handler)

		try:
			sserver.ThreadingTCPServer.__init__(self, ('0.0.0.0', self.PORT), RCHandler)
		except:
			logging.error('Unable to bind port %d' % self.PORT)
			sys.exit(1)

		self.serve_forever()

	def signal_handler(self, signum, frame):
		logging.info('Remote Control server stopped')
		sys.exit(0)


class RCHandler(sserver.BaseRequestHandler):

	def setup(self):
		pass

	def handle(self):
		raw = self.request.recv(1024)
		if not raw:
			return

		# clean all whitespace and decode as UTF8
		recv = raw.strip().decode('utf-8')

		# do some logging
		logging.debug("(%s) sent: %s" % (self.client_address, recv))
		
		# try parsing data as JSON
		try:
			data = json.loads(recv)
			print(data)
		except ValueError:
			logging.error('JSON parsing error: %s' % recv)
			return
		except:
			logging.error('Someting strange happened...')
			return
		
		# parse data
		if 'ctrl' in data:
			ctrl = data['ctrl']
			if ctrl == 'play':
				pass
			elif ctrl == 'pause':
				pass
			elif ctrl == 'stop':
				pass
		
#		print self.server.mediafinder.get_movies()



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
			print('Unknown command')
			sys.exit(2) # command line error		
		sys.exit(0)
	else:
		print('Usage: %s start|stop|restart|nod' % sys.argv[0])
		sys.exit(2)
