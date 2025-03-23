import random
import unittest
import sys

greetings = [
    "Hello there, wonderful world!",
    "Greetings, fellow earthling!",
    "Hey, you wonderful human!",
    "Top of the morning to you!",
    "Welcome to this magnificent day!",
    "Hey there, sunshine!",
    "Salutations from your friendly program!",
    "Well hello, fancy meeting you here!",
    "G'day mate!",
    "Howdy, partner!",
    "Welcome aboard the code express!",
    "Welcome aboard the code express again !"
    ]

def get_random_greeting():
    return random.choice(greetings)

if __name__ == "__main__":
    # Run the greeting
    print("\n=== Running the greeting program ===")
    print(get_random_greeting())
    
    # Run the tests
    print("\n=== Running the tests ===")
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover('.', pattern='test_*.py')
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(test_suite)
