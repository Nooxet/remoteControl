import dbus

sess = dbus.SessionBus()
proxy = sess.get_object(
