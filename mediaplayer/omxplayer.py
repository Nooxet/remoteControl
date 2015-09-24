#!/usr/bin/python

"""
An OMXPlayer class for controlling OMXPlayer
using the DBus protocol. Extends the superclass
MediaPlayer.

by Nox
2015
"""

import dbus
import getpass
import os
import logging
from mediaplayer import MediaPlayer

class OMXPlayer(MediaPlayer):

	def __init__(self, path = '.'):
		"""
		Calls superclass MediaPlayer to set up DBus connection.
		Create a DBus object and interfaces.
		"""
		MediaPlayer.__init__(self, path)

		# set up env. variables in order to find DBus paths
		try:
			username = getpass.getuser()
		except:
			logging.error('Could not find username in system')
			exit(1)

		dbus_path = '/tmp/omxplayerdbus.%s' % username
		dbus_pid_path = '%s.pid' % dbus_path

		# some error checking
		if not os.path.exists(dbus_path):
			logging.error('file "%s" not found' % dbus_path)
			exit(1)

		if not os.path.exists(dbus_pid_path):
			logging.error('file "%s" not found' % dbus_pid_path)
			exit(1)

		# read paths and export to env. variables
		with open(dbus_path, 'r') as f:
			dbus_data = f.read()
			os.environ['DBUS_SESSION_BUS_ADDRESS'] = dbus_data

		with open(dbus_pid_path, 'r') as f:
			dbus_pid_data = f.read()
			os.environ['DBUS_SESSION_BUS_PID'] = dbus_pid_data

		omxObject = self.dbusSession.get_object('org.mpris.MediaPlayer2.omxplayer',
			'/org/mpris/MediaPlayer2')
		self.omxIf = dbus.Interface(omxObject,
			dbus_interface='org.mpris.MediaPlayer2')
		self.omxPlayerIf = dbus.Interface(omxObject,
			dbus_interface='org.mpris.MediaPlayer2.Player')
		self.omxPropertiesIf = dbus.Interface(omxObject,
			dbus_interface='org.freedesktop.DBus.Properties')

	def play(self):
		"""Play the current media"""
		self.omxPlayerIf.Play()

	def pause(self):
		"""Pause the current media"""
		self.omxPlayerIf.Pause()

	def playPause(self):
		"""Play/Pause the current media"""
		self.omxPlayerIf.PlayPause()


if __name__ == '__main__':
	omxp = OMXPlayer()
	omxp.play()
