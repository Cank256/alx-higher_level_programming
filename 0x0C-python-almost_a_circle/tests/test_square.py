import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    def test_attributes(self):
        # Create a Square instance
        square = Square(5, 2, 3, 1)

        # Check attributes
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)

    def test_area(self):
        # Create a Square instance
        square = Square(5, 2, 3, 1)

        # Check the area calculation
        self.assertEqual(square.area(), 25)

    def test_str(self):
        # Create a Square instance
        square = Square(5, 2, 3, 1)

        # Check the string representation
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_size_setter(self):
        # Create a Square instance
        square = Square(5, 2, 3, 1)

        # Change the size using the setter
        square.size = 7

        # Check if width and height are updated
        self.assertEqual(square.size, 7)
        self.assertEqual(square.width, 7)
        self.assertEqual(square.height, 7)


if __name__ == '__main__':
    unittest.main()
