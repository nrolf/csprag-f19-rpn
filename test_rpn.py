import unittest
import rpn

class TestBasics(unittest.TestCase):
	def test_add(self):
		result = rpn.calculate('1 1 + ')
		self.assertEqual(2, result)
	def test_sub(self):
		result = rpn.calculate('5 3 -')
		self.assertEqual(2, result)
	def test_bad_input(self):
		with self.assertRaises(TypeError):
			rpn.calculate('1 2 3 +') 
	def test_carat(self):
		result = rpn.calculate('5 2 ^')
		self.assertEqual(25, result)

