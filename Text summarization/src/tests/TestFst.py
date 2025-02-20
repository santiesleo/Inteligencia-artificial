import unittest

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

from backend.FST.FstController import process_text_with_fst
from backend.FST.FstSynonyms import transformate_synonyms
from backend.FST.FstAntonyms import transformate_antonyms
from backend.FST.FstPronouns import *
from backend.FST.FstPastTenses import *
from backend.FST.FstFutureTenses import *
from backend.FST.FstPresentTenses import *

class TestFST(unittest.TestCase):
    
    def setUp(self):
        """
        Configuración inicial para todas las pruebas.
        """
        self.current_text1 = """Every day, I film scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all work together, and each person plays a vital role. He is handling the camera, while she is adjusting the lights. They are financing the project, ensuring we have enough funds to continue.

        I am careful when I film, trying to capture every detail. Sometimes, I fire questions at the actors to help them understand the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we work together to fix them."""
        
        self.setUpAntonyms()
        self.setUpSynonyms()
        self.setUpFutureTenses()
        self.setUpPastTenses()
        self.setUpPresentTenses()
        self.setUpPronouns()
    
    def setUpAntonyms(self):
        """Este método se ejecuta antes de cada caso de prueba."""
        self.fst_antonyms = transformate_antonyms()
        
    def setUpSynonyms(self):
        """Este método se ejecuta antes de cada caso de prueba."""
        self.fst_synonyms = transformate_synonyms()
        
    def setUpFutureTenses(self):
        """Este método se ejecuta antes de cada caso de prueba."""
        self.fst_future = create_fst_present_to_future_simple()
        
    def setUpPastTenses(self):
        """Este método se ejecuta antes de cada caso de prueba."""
        self.fst_present_to_past_simple = create_fst_present_to_past_simple()
        
    def setUpPresentTenses(self):
        """Este método se ejecuta antes de cada caso de prueba."""
        self.fst_present_to_continuous = create_fst_present_to_continuous()
        
    def setUpPronouns(self):
        """Este método se ejecuta antes de cada caso de prueba."""
        self.fst_pronouns_i = create_fst_pronouns_to_i()
        self.fst_pronouns_he = create_fst_pronouns_to_he()
        self.fst_pronouns_she = create_fst_pronouns_to_she()
        self.fst_pronouns_it = create_fst_pronouns_to_it()
        self.fst_pronouns_we = create_fst_pronouns_to_we()
        self.fst_pronouns_they = create_fst_pronouns_to_they()

    # Test cases for FSTs
    
    ## Synonyms
    def test_fst_synonyms_standard_case(self):
        current_text = process_text_with_fst(self.fst_synonyms, "The garden was filled with abundant flowers, their vibrant colors stretching as far as the eye could see.")
        acceptable_versions = ["The garden was filled with plentiful flowers, their vibrant colors stretching as far as the eye could see.", "The garden was filled with ample flowers, their vibrant colors stretching as far as the eye could see.", "The garden was filled with abundant flowers, their vibrant colors stretching as far as the eye could see."
        ]
    
        # Verificar si el texto actual coincide con alguna de las versiones aceptables
        self.assertTrue(current_text in acceptable_versions, f"{current_text} no coincide con ninguna versión aceptable.")
    
    def test_fst_synonyms_limiting_case(self):
        current_text = process_text_with_fst(self.fst_synonyms, "The cat is sleeping.")
        self.assertEqual(current_text, "The cat is sleeping.", "El texto debería quedar sin cambios.")
    
    def test_fst_synonyms_interesting_case(self):
        current_text = process_text_with_fst(self.fst_synonyms, "The beautiful, big garden was abundant with flowers.")
        acceptable_versions = [
        "The attractive, large garden was plentiful with flowers.",
        "The attractive, huge garden was ample with flowers.",
        "The attractive, huge garden was plentiful with flowers.",
        "The attractive, large garden was ample with flowers.",
        "The lovely, large garden was abundant with flowers.",
        "The lovely, large garden was ample with flowers.",
        "The lovely, huge garden was plentiful with flowers.",
        "The lovely, huge garden was ample with flowers.",
        "The beautiful, huge garden was ample with flowers.",
        "The beautiful, huge garden was plentiful with flowers.",
        "The beautiful, large garden was ample with flowers.",
        "The beautiful, large garden was plentiful with flowers."
        ]
        self.assertTrue(current_text in acceptable_versions, f"{current_text} no coincide con ninguna versión aceptable.")
    
    ## Antonyms
    def test_fst_antonyms_standard_case(self):
        current_text = process_text_with_fst(self.fst_antonyms, "The garden was filled with abundant flowers, their vibrant colors stretching as far as the eye could see.")
        acceptable_versions = ["The garden was filled with scarce flowers, their vibrant colors stretching as far as the eye could see.", "The garden was filled with limited flowers, their vibrant colors stretching as far as the eye could see.", "The garden was filled with meager flowers, their vibrant colors stretching as far as the eye could see."
        ]
        
        # Verificar si el texto actual coincide con alguna de las versiones aceptables
        self.assertTrue(current_text in acceptable_versions, f"{current_text} no coincide con ninguna versión aceptable.")
        
    def test_fst_antonyms_limiting_case(self):
        current_text = process_text_with_fst(self.fst_antonyms, "The sky is blue and the sun is shining.")
        self.assertEqual(current_text, "The sky is blue and the sun is shining.", "El texto debería quedar sin cambios cuando no hay coincidencias.")
    
    def test_fst_antonyms_interesting_case(self):
        current_text = process_text_with_fst(self.fst_antonyms, "The angry gardener had an abundant supply of seeds.")
        acceptable_versions = [
        "The calm gardener had an scarce supply of seeds.",
        "The calm gardener had an limited supply of seeds.",
        "The calm gardener had an meager supply of seeds.",
        "The peaceful gardener had an meager supply of seeds.",
        "The peaceful gardener had an limited supply of seeds.",
        "The peaceful gardener had an scarce supply of seeds.",
        "The calm gardener had an meager supply of seeds.",
        "The calm gardener had an scarce supply of seeds.",
        "The calm gardener had an limited supply of seeds.",
        "The happy gardener had an meager supply of seeds.",
        "The happy gardener had an scarce supply of seeds.",
        "The happy gardener had an limited supply of seeds."
        ]
        self.assertTrue(current_text in acceptable_versions, f"{current_text} no coincide con ninguna versión aceptable.")
    
    ## Future Tenses
    def test_fst_future_tenses_standard_case(self):
        current_text = process_text_with_fst(self.fst_future, "She dances gracefully and they are always amazed by her performance.")
        expected_text = "She will dance gracefully and they will be always amazed by her performance."
        self.assertEqual(current_text, expected_text, f"El texto transformado {current_text} no coincide con la versión esperada.")
    
    def test_fst_future_tenses_limiting_case(self):
        current_text = process_text_with_fst(self.fst_future, "The cat ventures on the couch every day.")
        self.assertEqual(current_text, "The cat ventures on the couch every day.", "El texto debería quedar sin cambios cuando no hay coincidencias.")
    
    def test_fst_future_tenses_interesting_case(self):
        current_text = process_text_with_fst(self.fst_future, self.current_text1)
        expected_text = "Every day, i will film scenes for my new project. The crew be always busy, and we will be filming from early morning until late at night. We will all work together, and each person play a vital role. He will be handling the camera, while she will be adjusting the lights. They will be financing the project, ensuring we will have enough fund to continue. i will be careful when i will film, trying to capture every detail. Sometimes, i will fire question at the actors to help them understand the scene better. The script be already fixed, but we will be always open to making small changes. When problems arise, we will work together to fix them."
        self.assertEqual(current_text, expected_text)
    
    ## Past Tenses
    ### Present to Past Simple
    def test_fst_present_to_past_simple_sentences_standard_case(self):
        current_text = process_text_with_fst(self.fst_present_to_past_simple, "I am dancing while they are watching.")
        expected_text = "I was dancing while they were watching."
        self.assertEqual(current_text, expected_text, f"El texto transformado {current_text} no coincide con la versión esperada.")
    
    def test_fst_present_to_past_simple_sentences_limiting_case(self):
        current_text = process_text_with_fst(self.fst_present_to_past_simple, "The dog barks at the mailman.")
        self.assertEqual(current_text, "The dog barks at the mailman.", "El texto debería quedar sin cambios cuando no hay coincidencias.")
    
    def test_fst_present_to_past_simple_sentences_interesting_case(self):
        current_text = process_text_with_fst(self.fst_present_to_past_simple, self.current_text1)
        expected_text = "Every day, I filmed scenes for my new project. The crew was always busy, and we were filming from early morning until late at night. We all worked together, and each person played a vital role. He was handling the camera, while she was adjusting the lights. They were financing the project, ensuring we have enough funded to continue. I was careful when I film, trying to captured every detail. Sometimes, I fired questioned at the actors to help them understood the scene better. The script was already fixed, but we were always open to making small changes. When problems arise, we worked together to fixed them."
        self.assertEqual(current_text, expected_text)
    
    ## Present Tenses
    def test_fst_present_tenses_standard_case(self):
        current_text = process_text_with_fst(self.fst_present_to_continuous, "Every day, I work and she admires the beauty.")
        expected_text = "Every day, i am working and she is admiring the beauty."
        self.assertEqual(current_text, expected_text, f"{current_text} no coincide con el texto esperado.")
    
    def test_fst_present_tenses_limiting_case(self):
        current_text = process_text_with_fst(self.fst_present_to_continuous, "The weather feels vibrant today.")
        expected_text = "The weather feels vibrant today."  # No hay verbos para transformar
        self.assertEqual(current_text, expected_text, f"{current_text} no coincide con el texto esperado.")
    
    def test_fst_present_tenses_interesting_case(self):
        current_text = process_text_with_fst(self.fst_present_to_continuous, self.current_text1)
        expected_text = "Every day, i am filming scenes for my new project. The crew  always busy, and we are  filming from early morning until late at night. We are all working together, and each person playing a vital role. He is  handling the camera, while she is  adjusting the lights. They are  financing the project, ensuring we are have enough funding to continue. i am  careful when i am film, trying to capturing every detail. Sometimes, i am firing questioning at the actors to help them understanding the scene better. The script  already fixed, but we are  always open to making small changes. When problems arise, we are working together to fixing them."
        self.assertEqual(current_text, expected_text)
    
    ## Pronouns
    ### I
    def test_fst_pronoun_i_standard_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_i, "He is going to the store, and she is buying groceries.")
        expected_text = "I am going to the store, and i am buying groceries."
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_i_limiting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_i, "They are going to the store.")
        expected_text = "They are going to the store." 
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_i_interesting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_i, self.current_text1)
        expected_text = "Every day, I film scenes for my new project. The crew am always busy, and we are filming from early morning until late at night. We all work together, and each person play a vital role. I am handling the camera, while i am adjusting the lights. They are financing the project, ensuring we have enough fund to continue. I am careful when I film, trying to capture every detail. Sometimes, I fire question at the actors to help them understand the scene better. The script am already fixed, but we are always open to making small changes. When problems arise, we work together to fix them."
        self.assertEqual(current_text, expected_text)
    
    ### He
    def test_fst_pronoun_he_standard_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_he, "She is handling the camera, while I am adjusting the settings. It amuses me how well she does her job.")
        expected_text = "He is handling the camera, while he is adjusting the settings. He amuses me how well he does her job."
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_he_limiting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_he, "I am")
        expected_text = "He is"
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_he_interesting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_he, self.current_text1)
        expected_text = "Every day, he films scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all works together, and each person plays a vital role. He is handling the camera, while he is adjusting the lights. They are financing the project, ensuring we have enough funds to continue. he is careful when he film, trying to captures every detail. Sometimes, he fires questions at the actors to help them understands the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we works together to fixes them."
        self.assertEqual(current_text, expected_text)
    
    ### She
    def test_fst_pronoun_she_standard_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_she, self.current_text1)
        expected_text = "Every day, she films scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all works together, and each person plays a vital role. He is handling the camera, while she is adjusting the lights. They are financing the project, ensuring we have enough funds to continue. she is careful when she film, trying to captures every detail. Sometimes, she fires questions at the actors to help them understands the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we works together to fixes them."
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_she_limiting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_she, "I am")
        expected_text = "She is"
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_she_interesting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_she, "He is handling the camera, while I am adjusting the settings. It is fascinating to see how it works.")
        expected_text = "He is handling the camera, while she is adjusting the settings. She is fascinating to sees how she works."
        self.assertEqual(current_text, expected_text)
    
    ### It
    def test_fst_pronoun_it_standard_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_it, self.current_text1)
        expected_text = "Every day, it films scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all works together, and each person plays a vital role. He is handling the camera, while it is adjusting the lights. They are financing the project, ensuring we have enough funds to continue. it is careful when it film, trying to captures every detail. Sometimes, it fires questions at the actors to help them understands the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we works together to fixes them."
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_it_limiting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_it, "I am")
        expected_text = "It is"
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_it_interesting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_it, "She is handling the camera, and he is adjusting the lights. I am watching.")
        expected_text = "It is handling the camera, and he is adjusting the lights. It is watching."
        self.assertEqual(current_text, expected_text)
    
    ### We
    def test_fst_pronoun_we_standard_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_we, "They are going to the store, and they will buy groceries.")
        expected_text = "We are going to the store, and we will buy groceries."  # Todas las ocurrencias de "they" deben cambiarse a "we"
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_we_limiting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_we, "She is going to the store.")
        expected_text = "She is going to the store."  # Ningún cambio debe ocurrir
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_we_interesting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_we, self.current_text1)
        expected_text = "Every day, I film scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all work together, and each person play a vital role. He is handling the camera, while she is adjusting the lights. We are financing the project, ensuring we have enough fund to continue. I am careful when I film, trying to capture every detail. Sometimes, I fire question at the actors to help them understand the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we work together to fix them."
        self.assertEqual(current_text, expected_text)
    
    ### They
    def test_fst_pronoun_they_standard_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_they, "We are going to the store, and we will buy groceries.")
        expected_text = "They are going to the store, and they will buy groceries."
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_they_limiting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_they, "He is going to the store.")
        expected_text = "He is going to the store."
        self.assertEqual(current_text, expected_text)
    
    def test_fst_pronoun_they_interesting_case(self):
        current_text = process_text_with_fst(self.fst_pronouns_they, self.current_text1)
        expected_text = "Every day, I film scenes for my new project. The crew is always busy, and they are filming from early morning until late at night. They all work together, and each person play a vital role. He is handling the camera, while she is adjusting the lights. They are financing the project, ensuring they have enough fund to continue. I am careful when I film, trying to capture every detail. Sometimes, I fire question at the actors to help them understand the scene better. The script is already fixed, but they are always open to making small changes. When problems arise, they work together to fix them."
        self.assertEqual(current_text, expected_text)
    
if __name__ == '__main__':
    unittest.main()