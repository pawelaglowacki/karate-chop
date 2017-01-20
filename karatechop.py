class Karate:
	def init(self):
		pass

	def chop(self, toFind, array):
		index = len(array)/2		
		if toFind == array[index]:
			return index
		return -1

