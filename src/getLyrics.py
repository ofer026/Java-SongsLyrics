try:
	import lyricwikia 
except ModuleNotFoundError:
	import os
	os.system("pip install lyricwikia")
	import lyricwikia

class getLyrics():
	def __init__(self, artist, song):
		self.artist = artist
		self.song = song
	def get_lyrics(self):
		try:
			lyrics = lyricwikia.get_lyrics(self.artist, self.song)
		except Exception:
			print("Error!")
			return
		print(lyrics)
if __name__ == '__main__':
	import sys
	args = sys.argv
	lyrics = getLyrics(args[1], args[2])
	lyrics.get_lyrics()
	
		
