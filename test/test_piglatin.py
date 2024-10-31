import unittest
from piglatin import PigLatin
from error import PigLatinError

class TestPigLatin(unittest.TestCase):
    def test_get_phrase(self):
        translator = PigLatin("hello world")
        assert translator.get_phrase() == "hello world"

    def test_translate_empty(self):
        translator = PigLatin("")
        assert translator.translate() == "nil"

    def test_translate_vowel(self):
        assert PigLatin("any").translate() == "anynay"
        assert PigLatin("apple").translate() == "appleyay"
        assert PigLatin("ask").translate() == "askay"

    def test_translate_single_consonant(self):
        assert PigLatin("hello").translate() == "ellohay"

    def test_translate_multiple_consonants(self):
        assert PigLatin("known").translate() == "ownknay"


