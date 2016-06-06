from django.test import TestCase

# Create your tests here.
class SimpleTest(TestCase):
	"""docstring for SimpleTest"""
	def test_basic_addition(self):
		self.assertEqual(1 + 1 , 3)
		