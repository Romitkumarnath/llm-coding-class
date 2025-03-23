import unittest
from hello import get_random_greeting, greetings

class TestHello(unittest.TestCase):
    def test_get_random_greeting(self):
        # Test that the function returns a string
        greeting = get_random_greeting()
        self.assertIsInstance(greeting, str)
        
        # Test that the returned greeting is in our greetings list
        self.assertIn(greeting, greetings)
        
        # Test that the function returns different greetings on multiple calls
        # (though this is probabilistic, it's very unlikely to fail)
        greeting1 = get_random_greeting()
        greeting2 = get_random_greeting()
        greeting3 = get_random_greeting()
        
        # At least one of these should be different
        self.assertTrue(
            greeting1 != greeting2 or 
            greeting2 != greeting3 or 
            greeting1 != greeting3
        )

if __name__ == '__main__':
    unittest.main() 