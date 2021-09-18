import unittest
from Vector3 import Vector3
import math

class TestVector3(unittest.TestCase):

  def test_equals(self):
    self.assertEqual(Vector3(1, 1, 1), Vector3(1, 1, 1), "Should be equal!")

  def test_add(self):
    v1 = Vector3(1, 2, 3)
    v2 = Vector3(3, -4, 2)
    expected_result = Vector3(4, -2, 5)
    self.assertEqual(v1 + v2, expected_result, "Should be (4, -2, 5)")
  
  def test_subtract(self):
    v1 = Vector3(1, 2, 3)
    v2 = Vector3(3, -4, 2)
    expected_result = Vector3(-2, 6, 1)
    self.assertEqual(v1 - v2, expected_result, "Should be (-2, 6, 1)")

  def test_negate(self):
    v1 = Vector3(1, 2, 3)
    expected_result = Vector3(-1, -2, -3)
    self.assertEqual(-v1, expected_result, "Should be (-1, -2, -3)")
  
  def test_norm2(self):
    v1 = Vector3(3, 0, -4)
    expected_result = 5
    self.assertEqual(v1.norm2(), expected_result, "Should be 5")
  
  def text_normalize(self):
    v1 = Vector3(1, 1, 1)
    expected_result = Vector3(1 / math.sqrt(3), 1 / math.sqrt(3), 1 / math.sqrt(3))
    self.assertEqual(v1.normalize(), expected_result, "Should be (1.732, 1.732, 1.732)")
  
  def test_cross_product(self):
    v1 = Vector3(1, 2, 3)
    v2 = Vector3(3, -4, 2)
    expected_result = Vector3(16, 7, -10)
    self.assertEqual(Vector3.cross_product(v1, v2), expected_result, "Should be (16, 7, -10)")
  
  def test_dot_product(self):
    v1 = Vector3(1, 2, 3)
    v2 = Vector3(3, -4, 2)
    expected_result = 1
    self.assertEqual(Vector3.dot_product(v1, v2), expected_result, "Should be 0")

if __name__ == '__main__':
    unittest.main()
