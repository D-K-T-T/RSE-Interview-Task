import unittest
from fruity_vice_task.fruity_vice_api import FruityViceAPI

class TestFruityViceAPI(unittest.TestCase):
    def setUp(self):
        self.api = FruityViceAPI()

    def test_valid_fruit(self):
        """Test for valid fruit (In this case: 'banana')."""
        response = self.api.get_fruit_info("banana")
        self.assertIn("name", response)
        self.assertIn("id", response)
        self.assertIn("family", response)
        self.assertIn("sugar", response)
        self.assertIn("carbohydrates", response)
        self.assertNotIn("error", response)

    def test_invalid_fruit(self):
        """Test for non-existent fruit (In this case: 'wineberry').""" 
        response = self.api.get_fruit_info("wineberry")
        self.assertIn("error", response)

if __name__ == "__main__":
    unittest.main()
