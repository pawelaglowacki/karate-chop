class Karate:
	def init(self):
		pass

	def chop(self, toFind, array):

		arrayLeftBoundary, arrayRightBoundary, arrayMiddle = 0, len(array)-1, len(array)/2
		while (arrayLeftBoundary <= arrayRightBoundary) :
			
			if array[arrayMiddle] < toFind:
				arrayLeftBoundary = arrayMiddle
				arrayMiddle = (arrayMiddle+arrayRightBoundary)/2
			
			if array[arrayMiddle] > toFind:
				arrayRightBoundary = arrayMiddle
				arrayMiddle = (arrayMiddle+arrayLeftBoundary)/2		

			print str(arrayMiddle) + ' ' + str(array[arrayMiddle]) + ' ' + str(toFind)
			if array[arrayMiddle]  == toFind:
				return arrayMiddle
		return -1



