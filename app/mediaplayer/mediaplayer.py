import dbus

class MediaPlayer:
	"""
	A superclass for all media players.
	Provides the common interface for controlling
	the media players utilizing the DBus protocol.
	"""

	def __init__(self, path):
		"""
		Set up initial connection to the DBus
		"""
		self.dbusSession = dbus.SessionBus()

