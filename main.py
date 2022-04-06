output = []

def clearattribute():
	attribute = "NaN"

def cleartype():
	cmd = "NaN"

class parsing():
	def __init__ (self, type, value):
		self.type = type
		self.value = value

	def gettype(self):
		cleartype()
		cmd = input("cmd:")
		self.type = cmd

	def getattribute(self):
		clearattribute()
		attribute = input("attribute:")
		self.value = attribute
	
	def sorttype(self):
		if self.type == "p":
			output.append(self.value)



lines = parsing("NaN", "NaN")
lines.gettype()
lines.getattribute()
lines.sorttype()


for n in range (len(output)):
	print(str(output[n]))
