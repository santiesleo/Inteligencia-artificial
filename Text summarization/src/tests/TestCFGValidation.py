import unittest

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from backend.CFG.CFGValidation import validate, create_cfg, get_sentences, analyze_sentence

class TestCFGValidation(unittest.TestCase):
    
    def setUp(self):
        self.cfg = create_cfg()
    
    # Pruebas para el método get_sentences
    def test_get_sentences_standard_case(self):
        text = "I went to the market, and I bought some fruits."
        expected_output = ["I went to the market", "and I bought some fruits"]
        self.assertEqual(get_sentences(text), expected_output)

    def test_get_sentences_limiting_case(self):
        text = "He plays football every day"
        expected_output = ["He plays football every day"]
        self.assertEqual(get_sentences(text), expected_output)

    def test_get_sentences_interesting_case(self):
        text = "I am happy! She is running; They were sleeping, but now they are awake."
        expected_output = [
            "I am happy", 
            "She is running", 
            "They were sleeping", 
            "but now they are awake"
        ]
        self.assertEqual(get_sentences(text), expected_output)

    # Pruebas para el método create_cfg
    def test_create_cfg_standard_case(self):
        tokens = ["DET", "NOUN", "VERB"]
        self.assertTrue(self.cfg.contains(tokens))
        
    # Pruebas para el método analyze_sentence
    def test_analyze_sentence_standard_case(self):
        sentence = "The cat sits on the mat"

        is_valid, tagged = analyze_sentence(sentence, self.cfg)
        assert is_valid == True, "The sentence should be valid according to the CFG."
        
    def test_analyze_sentence_limiting_case(self):
        sentence = "The cat"
        is_valid, tagged = analyze_sentence(sentence, self.cfg)
        assert is_valid == False, "The sentence should not be valid according to the CFG."

    def test_analyze_sentence_interesting_case(self):
        sentence = "She ran to store"
        is_valid, tagged = analyze_sentence(sentence, self.cfg)
        assert is_valid == True, "The sentence should be valid according to the CFG."

    # Test Case 1: Standard Case
    def test_validate_standard_case(self):
        input_text = "They love me. The dog barked. She reads a book. He plays football."
        expected_output = [
            ["They love me", True, [('They', 'PRP'), ('love', 'VBP'), ('me', 'PRP')]], 
            ["The dog barked", True, [('The', 'DT'), ('dog', 'NN'), ('barked', 'VBD')]], 
            ["She reads a book", True, [('She', 'PRP'), ('reads', 'VBZ'), ('a', 'DT'), ('book', 'NN')]], 
            ["He plays football", True, [('He', 'PRP'), ('plays', 'VBZ'), ('football', 'NN')]]
        ]
        self.assertEqual(validate(input_text), expected_output)

    # Test Case 2: Limiting Case
    def test_validate_limiting_case(self):
        input_text = "The cat. The dog barks run and the. She he it now."
        expected_output = [
            ["The cat", False, [('The', 'DT'), ('cat', 'NN')]], 
            ["The dog barks run and the", False, [('The', 'DT'), ('dog', 'NN'), ('barks', 'NNS'), ('run', 'VBP'), ('and', 'CC'), ('the', 'DT')]], 
            ["She he it now", False, [('She', 'PRP'), ('he', 'PRP'), ('it', 'PRP'), ('now', 'RB')]]
        ]
        self.assertEqual(validate(input_text), expected_output)

    # Test Case 3: Interesting Case
    def test_validate_interesting_case(self):
        input_text = "The cat ran, the dog barked. She finished homework. They played soccer."
        expected_output = [
            ["The cat ran", True, [('The', 'DT'), ('cat', 'NN'), ('ran', 'VBD')]], 
            ["the dog barked", True, [('the', 'DT'), ('dog', 'NN'), ('barked', 'VBD')]], 
            ["She finished homework", True, [('She', 'PRP'), ('finished', 'VBD'), ('homework', 'NN')]], 
            ["They played soccer", True, [('They', 'PRP'), ('played', 'VBD'), ('soccer', 'NN')]]
        ]
        self.assertEqual(validate(input_text), expected_output)

if __name__ == '__main__':
    unittest.main()