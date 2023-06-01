"""
this module implements eng-2-fr and fr-2-end translator functions
"""
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    englisth to french translation function 
    """
    french_text = MyMemoryTranslator(source='en', target='fr').translate(english_text)
    return french_text

def french_to_english(french_text):
    """
    french to english translation function 
    """
    english_text = MyMemoryTranslator(source='fr', target='en').translate(french_text)
    return english_text
