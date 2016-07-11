
from __future__ import print_function
from __future__ import unicode_literals

import os
import subprocess
import json

from mediafinder import MediaFinder

class RemoteControl(object):

	def __init__(self):
		self.mediafinder = MediaFinder('/home/noxet/Movies')
		self.movies = []
		self.music = []
		self.process = None

	# TODO: some caching function in case nothing has been added or removed
	def get_movies(self):
		"""
		Saves the movies in a list and returns it as a JSON object.
		"""
		self.movies = self.mediafinder.get_movies()
		return self._jsonify(self.movies)

	def get_music(self):
		"""
		Saves the music in a list and returns it as a JSON object.
		"""
		self.music = self.mediafinder.get_music()
		return self._jsonify(self.music)

	def _jsonify(self, media):
		"""
		Returns a JSON object of a list, with index as key.
		"""
		# add movies to dictionary with index as key
		media_json = dict()
		for i in range(len(media)):
			# remove the path, get only the movie title
			media_title = os.path.basename(os.path.normpath(media[i]))
			media_json[str(i)] = media_title

		try:
			media_json = json.dumps(media_json)
		except ValueError:
			print("got value error")
			return None
		except Exception:
			print("Something else happened...")
			return None

		return media_json

	def play(self, idx):
		idx = int(idx)
		self.process = subprocess.Popen(['/usr/bin/mplayer', self.movies[idx]],
			stdin=subprocess.PIPE)

	def pause(self):
		self.process.stdin.write('p')

	def stop(self):
		pass


if __name__ == '__main__':
	rc = RemoteControl()
	print(rc.get_movies())
