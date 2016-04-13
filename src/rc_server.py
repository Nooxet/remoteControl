
from __future__ import print_function
from __future__ import unicode_literals

from bottle import route, run, template

from remotecontrol import RemoteControl

rc = RemoteControl()

@route('/movies/get')
def movies_get():
	return rc.get_movies()

@route('/movies/play/<idx>')
def movies_play(idx):
	rc.play(idx)

@route('/movies/pause')
def movies_pause():
	rc.pause()

@route('/music/get')
def music_get():
	return rc.get_music()

run(host='localhost', port=8080)
