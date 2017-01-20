class Karate:
	def init(self):
		pass

	def chop(self, toFind, array):

		arrayLeftBoundary, arrayRightBoundary, arrayMiddle = 0, len(array)-1, len(array)/2
		
		while(arrayLeftBoundary < arrayRightBoundary):
			if toFind < array[arrayMiddle]:
				arrayRightBoundary = arrayRightBoundary - arrayMiddle
				arrayMiddle = (arrayLeftBoundary + arrayRightBoundary)/2						
			if array[arrayMiddle] < toFind:
				arrayLeftBoundary = arrayLeftBoundary + arrayMiddle
				arrayMiddle = (arrayLeftBoundary + arrayRightBoundary)/2						
			if array[arrayMiddle] == toFind:
				return arrayMiddle

		if array[arrayMiddle] == toFind:
			return arrayMiddle
		return -1



