from pyformlang.finite_automaton import DeterministicFiniteAutomaton, State, Symbol

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from text_processing.Preprocessor import Preprocessor
class DFASummarizer:
    def __init__(self, keywords):
        """
        Inicializa el DFA para buscar las palabras clave en las oraciones.
        """
        self.keywords = keywords
        self.dfa = self.build_dfa(keywords)

    def build_dfa(self, keywords):
        """
        Construye un DFA a partir de las palabras clave.
        Cada palabra clave genera un estado final si es reconocida.
        """
        dfa = DeterministicFiniteAutomaton()
        start_state = State(0) 
        dfa.add_start_state(start_state)

        # Transición desde el estado inicial para cada palabra clave
        for i, keyword in enumerate(keywords):
            keyword_state = State(i + 1)  # Estado único para cada palabra clave
            dfa.add_transition(start_state, Symbol(keyword), keyword_state)
            dfa.add_final_state(keyword_state)  # Cada estado que reconoce una palabra clave es final

        return dfa
    
    def summarize_text(self, sentences):
        """
        Procesa las oraciones, busca las palabras clave usando el DFA
        y retorna un resumen con las oraciones que contienen palabras clave.
        """
        summary = []
        preprocessor = Preprocessor()

        for sentence in sentences:
            tokens = preprocessor.tokenize_text(sentence)  # Tokenizar cada oración
            current_state = self.dfa.start_state  # Iniciamos en el estado inicial

            # Verificamos si alguna palabra clave está presente en los tokens de la oración
            for token in tokens:
                if self.dfa.accepts([Symbol(token)]):  # Si el token es aceptado por el DFA
                    summary.append(sentence + ". ")  # Agregamos la oración al resumen
                    break # Pasamos a la siguiente oración
        return summary