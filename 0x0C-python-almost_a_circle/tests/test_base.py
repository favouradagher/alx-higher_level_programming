import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_base_instance_creation(self):
        """Test creating an instance of Base."""
        obj = Base()
        self.assertIsInstance(obj, Base)

    def test_base_id_generation(self):
        """Test if the ID is generated correctly."""
        obj1 = Base()
        obj2 = Base()
        obj3 = Base()
        self.assertEqual(obj1.id, 1)
        self.assertEqual(obj2.id, 2)
        self.assertEqual(obj3.id, 3)

    def test_base_id_custom_value(self):
        """Test setting a custom ID value."""
        obj = Base(10)
        self.assertEqual(obj.id, 10)

    def test_base_id_negative_value(self):
        """Test setting a negative custom ID value."""
        with self.assertRaises(ValueError):
            obj = Base(-1)

if __name__ == "__main__":
    unittest.main()

