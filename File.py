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
		
		