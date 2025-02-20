# Clase para procesar el texto
import re

class Preprocessor:
    def __init__(self):
        pass
    
    def split_sentences(self, text):
        """
        Divide el texto en oraciones basadas en puntos y signos de interrogación.
        """
        sentence_pattern = r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s'
        sentences = re.split(sentence_pattern, text)
        # Eliminar el punto al final de cada oración si existe
        return [sentence.rstrip('.').strip() for sentence in sentences]

    def extract_proper_nouns(self, text):
        """
        Extrae sustantivos propios (palabras que inician con mayúscula) 
        excluyendo pronombres y otras palabras que no sean proper nouns reales.
        """
        proper_noun_pattern = r'\b[A-Z][a-z]*\b'
        # Lista de palabras que no deberían considerarse proper nouns
        common_exceptions = {"The", "This", "That", "A", "An", "In", "On", "For", "Is", "Of", "And"}

        # Extraer todas las palabras que inician con mayúscula
        all_proper_nouns = re.findall(proper_noun_pattern, text)
        
        # Filtrar las palabras que están en la lista de excepciones
        filtered_proper_nouns = [word for word in all_proper_nouns if word not in common_exceptions]

        return filtered_proper_nouns

    def extract_keywords(self, text, keywords):
        """
        Extrae palabras clave del texto, basadas en una lista predefinida.
        """
        keyword_pattern = r'\b(?:' + '|'.join(re.escape(word) for word in keywords) + r')\b'
        found_keywords = re.findall(keyword_pattern, text)
        # Convertimos a un set para eliminar duplicados, y luego a una lista para preservar el orden
        return list(dict.fromkeys(found_keywords))

    def tokenize_text(self, text):
        """
        Tokeniza el texto dividiéndolo en palabras.
        """
        return re.findall(r'\b\w+\b', text)