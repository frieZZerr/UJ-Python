import fracs
import unittest

class TestFractions(unittest.TestCase):
	def setUp(self):
		self.zero = [0, 1]

	def test_add_frac(self):
		self.assertEqual( fracs.add_frac([1, 2], [1, 3]), [5, 6] )

	def test_sub_frac(self):
		self.assertEqual( fracs.sub_frac([1, 2], [1, 3]), [1, 6] )

	def test_mul_frac(self):
		self.assertEqual( fracs.mul_frac([5, 2], [1, 3]), [5, 6] )

	def test_div_frac(self):
		self.assertEqual( fracs.div_frac([5, 2], [1, 3]), [15, 2] )

	def test_is_positive(self):
		self.assertEqual( fracs.is_positive(self.zero), False )

	def test_is_zero(self):
		self.assertEqual( fracs.is_zero(self.zero), True )

	def test_cmp_frac(self):
		self.assertEqual( fracs.cmp_frac([1, 2], [1, 3]), -1 )

	def test_frac2float(self):
		self.assertEqual( fracs.frac2float([5, 2]), 2.5 )

if __name__ == '__main__':
	unittest.main()