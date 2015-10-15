#!/usr/bin/python

import os

class MediaFinder:
	
	def __init__(self, path = '.'):
		self.path = path
		self.movieext = [".mp4", ".mkv", ".avi"]
		self.movies = []
		self.musicext = [".mp3", ".wma", ".flac"]
		self.music = []
		

	def get_movies(self):
		"""
		Returns a list with all movie files
		"""
		for root, dirs, files in os.walk(self.path):
			for file in files:
				name, ext = os.path.splitext(file)
				if ext in self.movieext:
					self.movies.append(name)
		
		return self.movies
		
	def get_music(self):
		"""
		Returns a list with all music files
		"""
		for root, dirs, files in os.walk(self.path):
			for file in files:	
				name, ext = os.path.splitext(file)
				if ext in self.musicext:
					self.music.append(name)
						
		return self.music
			
		
					
			
		
		
		

if __name__ == '__main__':
	# create a media finder object, with path = 'mypath'
	mf = MediaFinder('C:\\Users\\Andreas\\Desktop\\')

	# prints the list with all media
	# print mf.get_movies()
	print mf.get_music()
	
	
	

	
