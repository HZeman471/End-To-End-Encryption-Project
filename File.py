import os
class File:
	FileName = ""
	Directory = ""
	Alias = ""
	def __init__(self, Direectory):
		self.Direectory = Direectory
		self.FileName = os.path.basename(Direectory)
	
	def __init__(self):
		self.Direectory = -1
		self.FileName = -1
		self.Alias = -1
	
	def AssimilateFromPair(self, FileLine):
		self.Alias, self.FileName = FileLine.split(", ")
		self.Direectory = r"C:\Users\Hrvoje\OneDrive - Univerza v Mariboru\Namizje\Library of Congress\Moji prispevki\AES Enkripcija\uploads" # TODO: Good grief, someone fix this