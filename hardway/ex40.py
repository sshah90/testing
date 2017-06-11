class Song(object):

	def __init__(self,data):
		self.lyrics=lyrics
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bady = Song(["Happy birthday to you","I don't want to get sued","So I'will stop right there"])

bulls_on_parade=Song(["they rally around the family","with pockets full of shells"])

happy_bady.sing_me_a_song()
bulls_on_parade.sing_me_a_song()