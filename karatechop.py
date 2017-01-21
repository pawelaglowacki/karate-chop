class Karate:
	def init(self):
		pass

	def chop(self, toFind, array):

		if len(array)<=0:
			 return -1

		left = 0
		right = len(array)-1
		middle = (left + right) / 2
	
		while left <= right:	
			if(array[middle] is toFind):
				return middle
			
			if(array[middle] < toFind):
				left = middle + 1
				middle = (left + right) / 2

			if(array[middle] > toFind):
				right = middle - 1
				middle = (left + right) / 2

		return -1
