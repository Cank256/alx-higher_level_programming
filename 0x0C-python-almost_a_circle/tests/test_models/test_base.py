import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    def test_id_incrementation(self):
        # Create two Base instances without specifying an id
        base1 = Base()
        base2 = Base()

        # Check that their ids are incremented
        self.assertEqual(base1.id, 1)
        self.assertEqual(base2.id, 2)

    def test_id_assignment(self):
        # Create a Base instance with a specific id
        base = Base(100)

        # Check that the specified id is assigned
        self.assertEqual(base.id, 100)


if __name__ == '__main__':
    unittest.main()
