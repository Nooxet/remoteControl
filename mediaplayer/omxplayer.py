#!/usr/bin/python

"""
An OMXPlayer class for controlling OMXPlayer
using the DBus protocol. Extends the superclass
MediaPlayer.

by Nox
2015
"""

import dbus
from mediaplayer import MediaPlayer

class OMXPlayer(MediaPlayer):

	def __init__(self, path = '.'):
		"""
		Calls superclass MediaPlayer to set up DBus connection.
		Create a DBus object and interfaces.
		"""
		MediaPlayer.__init__(self, path)

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
