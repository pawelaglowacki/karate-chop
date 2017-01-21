import unittest
import karatechop

class TestKarateChop(unittest.TestCase):

	def setUp(self):
		self.karate = karatechop.Karate()

	def test_notFound(self):
		self.assertEqual(-1, self.karate.chop(4, []))
		self.assertEqual(-1, self.karate.chop(4, [1]))
		self.assertEqual(-1, self.karate.chop(4, [10,20]))
		self.assertEqual(-1, self.karate.chop(100, range(1,50)))
		self.assertEqual(-1, self.karate.chop(0, range(1,50)))
		

	def test_found_in_the_middle(self):
		self.assertEqual(0, self.karate.chop(4, [4]))
		self.assertEqual(1, self.karate.chop(10, [0,10,11]))
		self.assertEqual(1, self.karate.chop(10, [0,10,11,999]))
		self.assertEqual(2, self.karate.chop(11, [0,10,11,999]))

	def test_extreme_values(self):
		self.assertEqual(0, self.karate.chop(11, [11,12,15,999]))
		self.assertEqual(10, self.karate.chop(15, [0,1,2,3,4,5,6,7,10,11,15]))



if __name__ == '__main__':
	unittest.main()
