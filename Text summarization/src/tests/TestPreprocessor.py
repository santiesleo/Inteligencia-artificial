import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from backend.text_processing.Preprocessor import *


import unittest

class TestPreprocessor(unittest.TestCase):

    def setUp(self):
        # Crear una instancia del preprocesador antes de cada prueba
        self.preprocessor = Preprocessor()
        
        # Configurar textos de ejemplo para usar en las pruebas
        self.text_standard = "Every day, I film scenes for my new project. The crew is always busy."
        self.text_with_abbreviation = "Dr. Smith works in the U.S.A. He is a well-known doctor."
        self.text_empty = ""
        self.keywords = ["film", "project", "busy"]

    # --- Test para split_sentences ---

    def test_split_sentences_standard_case(self):
        # Standard case: oración común con punto final
        expected_output = ["Every day, I film scenes for my new project", "The crew is always busy"]
        self.assertEqual(self.preprocessor.split_sentences(self.text_standard), expected_output)
    
    def test_split_sentences_interesting_case(self):
        # Interesting case: texto con abreviaturas
        expected_output = ["Dr. Smith works in the U.S.A. He is a well-known doctor"]
        self.assertEqual(self.preprocessor.split_sentences(self.text_with_abbreviation), expected_output)

    def test_split_sentences_edge_case(self):
        # Edge case: texto vacío
        expected_output = [""]
        self.assertEqual(self.preprocessor.split_sentences(self.text_empty), expected_output)

    # --- Test para extract_proper_nouns ---

    def test_extract_proper_nouns_standard_case(self):
        # Standard case: texto con nombres propios estándar
        text = "John and Mary work at Google."
        expected_output = ["John", "Mary", "Google"]
        self.assertEqual(self.preprocessor.extract_proper_nouns(text), expected_output)

    def test_extract_proper_nouns_interesting_case(self):
        # Interesting case: texto con excepciones y palabras en mayúscula que no son sustantivos propios
        text = "This is The Best Day Ever In History."
        expected_output = ["Best", "Day", "Ever", "History"]
        self.assertEqual(self.preprocessor.extract_proper_nouns(text), expected_output)

    def test_extract_proper_nouns_edge_case(self):
        # Edge case: texto sin palabras en mayúscula
        text = "the quick brown fox jumps over the lazy dog."
        expected_output = []
        self.assertEqual(self.preprocessor.extract_proper_nouns(text), expected_output)

    # --- Test para extract_keywords ---

    def test_extract_keywords_standard_case(self):
        # Standard case: palabras clave encontradas en el texto
        expected_output = ["film", "project", "busy"]
        self.assertEqual(self.preprocessor.extract_keywords(self.text_standard, self.keywords), expected_output)

    def test_extract_keywords_interesting_case(self):
        # Interesting case: palabras clave repetidas en el texto
        text_with_repeats = "I film scenes for my project. The project is always busy."
        expected_output = ["film", "project", "busy"]
        self.assertEqual(self.preprocessor.extract_keywords(text_with_repeats, self.keywords), expected_output)

    def test_extract_keywords_edge_case(self):
        # Edge case: ningún keyword encontrado
        text_no_keywords = "I read books and write articles."
        expected_output = []
        self.assertEqual(self.preprocessor.extract_keywords(text_no_keywords, self.keywords), expected_output)

    # --- Test para tokenize_text ---

    def test_tokenize_text_standard_case(self):
        # Standard case: texto con palabras comunes
        expected_output = ["Every", "day", "I", "film", "scenes", "for", "my", "new", "project", "The", "crew", "is", "always", "busy"]
        self.assertEqual(self.preprocessor.tokenize_text(self.text_standard), expected_output)

    def test_tokenize_text_interesting_case(self):
        # Interesting case: texto con signos de puntuación y números
        text_with_punctuation = "I have $100.50 in my account, but I owe 20% to the bank."
        expected_output = ["I", "have", "100", "50", "in", "my", "account", "but", "I", "owe", "20", "to", "the", "bank"]
        self.assertEqual(self.preprocessor.tokenize_text(text_with_punctuation), expected_output)

    def test_tokenize_text_edge_case(self):
        # Edge case: texto vacío
        expected_output = []
        self.assertEqual(self.preprocessor.tokenize_text(self.text_empty), expected_output)


if __name__ == '__main__':
    unittest.main()
