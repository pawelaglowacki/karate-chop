import unittest
import karatechop

class TestKarateChop(unittest.TestCase):

	def setUp(self):
		self.karate = karatechop.Karate()

	def test_sample(self):
		self.assertEqual(-1, self.karate.chop(4, [1,2,3]))
		

if __name__ == '__main__':
	unittest.main()
