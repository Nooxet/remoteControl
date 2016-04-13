#!/usr/bin/python

from __future__ import print_function
from __future__ import unicode_literals

import os

class MediaFinder:
	
	def __init__(self, path = '.'):
		self.path = path
		self.movieext = [".mp4", ".mkv", ".avi"]
		self.musicext = [".mp3", ".wma", ".flac"]


	def get_media(self, mediaext):
		"""
		Returns a list with all media files
		"""
		medialist = []
		for root, dirs, files in os.walk(self.path):
			for fil in files:
				name, ext = os.path.splitext(fil)
				# only add requested media
				if ext in mediaext:
					medialist.append(root + "/" +  fil)

		return medialist
		
	def get_music(self):
		"""
		Returns a list with all music files
		"""
		return self.get_media(self.musicext)
		
	def get_movies(self):
		"""
		Returns a list with all movies files
		"""
		return self.get_media(self.movieext)


if __name__ == '__main__':
	# create a media finder object, with path = 'mypath'
	mf = MediaFinder('/home/noxet/Movies')

	# prints the list with all media
	# print mf.get_movies()
	print("music:", mf.get_music())
	print("filmer:", mf.get_movies())
