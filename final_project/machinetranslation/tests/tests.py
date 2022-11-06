"""
Import unittest to get test results.
"""
import unittest
from translator import english_to_french, french_to_english

class TestTranslatorE2F(unittest.TestCase):
    """
    This identify TestCase from TestTranslatorE2F.
    """
    def test_english_to_french(self):
        """
        This function tests English to French.
        """
        self.assertNotEqual(english_to_french("None"), '')
        #test when null is given as input the output must not be an empty string.
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        #test when the string 'Hello' is given as input the output must be 'Bonjour'.

class TestTranslatorF2E(unittest.TestCase):
    """
    This identify TestCase from TestTranslatorF2E.
    """
    def test_french_to_english(self):
        """
        This function tests French to English.
        """
        self.assertNotEqual(french_to_english("None"), '')
        #test when null is given as input the output must not be an empty string.
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        #test when the string 'Bonjour' is given as input the output must be 'Hello'.

if __name__ == "__main__":
    unittest.main()
    