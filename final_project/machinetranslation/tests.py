import unittest
from translator import englishToFrench, frenchToEnglish

class TestEnglish2French(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(englishToFrench('english'),'anglaise')
        self.assertEqual(englishToFrench('cat'),'chat')

class TestFrench2English(unittest.TestCase):
    def frenchToEnglish(self):
        self.assertEqual(frenchToEnglish('français'),'french')
        self.assertEqual(frenchToEnglish('chien'),'dog')

unittest.main()