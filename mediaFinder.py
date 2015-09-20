#!/usr/bin/python

import os

class MediaFinder:

	def __init__(self, path = '.'):
		pass

	def get_media(self):
		"""
		Returns a list with all media files
		"""
		pass

if __name__ == '__main__':
	# create a media finder object, with path = 'mypath'
	mf = MediaFinder('mypath')

	# prints the list with all media
	print mf.get_media()
