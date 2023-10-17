import unittest
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_square_instance_creation(self):
        """Test creating an instance of Square."""
        obj = Square(5)
        self.assertIsInstance(obj, Square)

    def test_square_attributes(self):
        """Test if attributes are set correctly."""
        obj = Square(5, 2, 3, 42)
        self.assertEqual(obj.size, 5)
        self.assertEqual(obj.x, 2)
        self.assertEqual(obj.y, 3)
        self.assertEqual(obj.id, 42)

    def test_square_area(self):
        """Test the area calculation."""
        obj = Square(4)
        self.assertEqual(obj.area(), 16)

    def test_square_str_representation(self):
        """Test the __str__ method."""
        obj = Square(3, 1, 2, 7)
        self.assertEqual(str(obj), "[Square] (7) 1/2 - 3")

    def test_square_update_attributes(self):
        """Test updating attributes using update method."""
        obj = Square(5, 2, 3, 8)
        obj.update(10)
        self.assertEqual(obj.id, 10)
        obj.update(10, 3)
        self.assertEqual(obj.size, 3)
        obj.update(10, 3, 4)
        self.assertEqual(obj.x, 3)
        obj.update(10, 3, 4, 5)
        self.assertEqual(obj.y, 4)

if __name__ == "__main__":
    unittest.main()

