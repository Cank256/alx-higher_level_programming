import unittest
from models.rectangle import Rectangle


class TestRectangleValidation(unittest.TestCase):
    def test_valid_attributes(self):
        # Test with valid attributes
        rect = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_invalid_attributes(self):
        # Test with invalid attributes
        with self.assertRaises(TypeError):
            Rectangle("5", 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3, 1)
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3, 1)


if __name__ == '__main__':
    unittest.main()
