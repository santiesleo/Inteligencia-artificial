import unittest

from pyformlang.finite_automaton import Symbol

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from backend.text_summarization.DFASummarizer import DFASummarizer

class TestDFASummarizer(unittest.TestCase):

    def setUp(self):
        # Palabras clave para inicializar el DFA
        self.keywords = ["film", "project", "camera", "finance"]
        
        # Instancia de DFASummarizer
        self.dfa_summarizer = DFASummarizer(self.keywords)
        
        # Oraciones de prueba
        self.sentences_standard = [
            "I film scenes for my project",
            "The camera is essential to this process",
            "We work from early morning to late at night"
        ]
        self.sentences_with_extra_keywords = [
            "I film for my project with a new camera",
            "The finance team is working hard"
        ]
        self.sentences_empty = []

    # --- Test para build_dfa ---

    def test_build_dfa_edge_case(self):
        # Edge case: Lista vacía de palabras clave
        empty_keywords = []
        dfa_summarizer = DFASummarizer(empty_keywords)
        dfa = dfa_summarizer.build_dfa(empty_keywords)

        # Verificar que no haya estados finales
        self.assertEqual(dfa._final_states, set())  # No debe haber estados finales

    # --- Test para summarize_text ---

    def test_summarize_text_standard_case(self):
        # Standard case: Resumir texto con palabras clave presentes
        summary = self.dfa_summarizer.summarize_text(self.sentences_standard)
        expected_summary = [
            "I film scenes for my project. ",
            "The camera is essential to this process. "
        ]
        self.assertEqual(summary, expected_summary)

    def test_summarize_text_interesting_case(self):
        # Interesting case: Texto con palabras clave adicionales
        summary = self.dfa_summarizer.summarize_text(self.sentences_with_extra_keywords)
        expected_summary = [
            "I film for my project with a new camera. ",
            "The finance team is working hard. "
        ]
        self.assertEqual(summary, expected_summary)

    def test_summarize_text_edge_case(self):
        # Edge case: Texto vacío
        summary = self.dfa_summarizer.summarize_text(self.sentences_empty)
        expected_summary = []  # No debe haber ningún resumen
        self.assertEqual(summary, expected_summary)

if __name__ == '__main__':
    unittest.main()
