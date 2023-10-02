import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_attributes(self):
        # Create a Rectangle instance
        rect = Rectangle(5, 10, 2, 3, 1)

        # Check the attributes
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 2)
        self.assertEqual(rect.y, 3)

    def test_validators(self):
        # Test invalid width, height, x, and y values
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
