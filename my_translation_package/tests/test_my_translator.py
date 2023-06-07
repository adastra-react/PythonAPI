import unittest
from my_translation_package import my_translator

class TestMyTranslator(unittest.TestCase):

    def test_english_to_french(self):
        self.assertEqual(my_translator.english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(my_translator.english_to_french("Hello"), "Hello")

    def test_french_to_english(self):
        self.assertEqual(my_translator.french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(my_translator.french_to_english("Bonjour"), "Bonjour")

if __name__ == '__main__':
    unittest.main()
