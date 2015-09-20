import dbus

class DBusControl:

	def __init__(self, path):
		# connect to the session bus
		session = dbus.SessionBus()

