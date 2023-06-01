import unittest
from translator import english_to_french, french_to_english

class TestEnglish2French(unittest.TestCase):
    def test_english_to_french(self):
        self.assertEqual(english_to_french('sun'),'soleil')
        self.assertNotEqual(english_to_french('cat'),'chien')

class TestFrench2English(unittest.TestCase):
    def test_french_to_english(self):
        self.assertEqual(french_to_english('lune'),'moon')
        self.assertNotEqual(french_to_english('chat'),'dog')

unittest.main()