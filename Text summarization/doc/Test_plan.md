# Test Plan for Text Summarization and Processing

## Test Plan for DFASummarizer

## 1. Method: `build_dfa`

### Test Case 1: Standard Case
- **Scenario**: Build DFA with a standard list of keywords.
- **Input**: 
  ```python
  keywords = ["film", "project", "camera", "finance"]
  ```
- **Expected Output**: A DFA with valid states and transitions representing the input keywords.

### Test Case 2: Edge Case
- **Scenario**: Build DFA with an empty list of keywords.
- **Input**: 
  ```python
  empty_keywords = []
  ```
- **Expected Output**: 
  ```python
  dfa._final_states  # Should return an empty set
  ```

### Test Case 3: Interesting Case
- **Scenario**: Build DFA with keywords that have partial similarities.
- **Input**: 
  ```python
  composed_keywords = ["camera", "cameraman"]
  ```
- **Expected Output**: A DFA that correctly differentiates between "camera" and "cameraman".

---

## 2. Method: `summarize_text`

### Test Case 1: Standard Case
- **Scenario**: Summarize text containing defined keywords.
- **Input**: 
  ```python
  sentences = [
      "I film scenes for my project",
      "The camera is essential to this process",
      "We work from early morning to late at night"
  ]
  ```
- **Expected Output**: 
  ```python
  ["I film scenes for my project. ", "The camera is essential to this process. "]
  ```

### Test Case 2: Edge Case
- **Scenario**: Summarize empty text.
- **Input**: 
  ```python
  sentences = []
  ```
- **Expected Output**: 
  ```python
  []  # No summary should be returned
  ```

### Test Case 3: Interesting Case
- **Scenario**: Summarize text with additional keywords.
- **Input**: 
  ```python
  sentences = [
      "I film for my project with a new camera",
      "The finance team is working hard"
  ]
  ```
- **Expected Output**: 
  ```python
  ["I film for my project with a new camera. ", "The finance team is working hard. "]
  ```

---

## Test Plan for Preprocessor

---

## 1. Method: `split_sentences`

### Test Case 1: Standard Case
- **Scenario**: Split a standard sentence with a proper ending.
- **Input**: 
  ```python
  text = "Every day, I film scenes for my new project. The crew is always busy."
  ```
- **Expected Output**: 
  ```python
  ["Every day, I film scenes for my new project", "The crew is always busy"]
  ```

### Test Case 2: Interesting Case
- **Scenario**: Split text containing abbreviations.
- **Input**: 
  ```python
  text = "Dr. Smith works in the U.S.A. He is a well-known doctor."
  ```
- **Expected Output**: 
  ```python
  ["Dr. Smith works in the U.S.A. He is a well-known doctor"]
  ```

### Test Case 3: Edge Case
- **Scenario**: Split an empty text.
- **Input**: 
  ```python
  text = ""
  ```
- **Expected Output**: 
  ```python
  [""]
  ```

---

## 2. Method: `extract_proper_nouns`

### Test Case 1: Standard Case
- **Scenario**: Extract proper nouns from a text with standard names.
- **Input**: 
  ```python
  text = "John and Mary work at Google."
  ```
- **Expected Output**: 
  ```python
  ["John", "Mary", "Google"]
  ```

### Test Case 2: Interesting Case
- **Scenario**: Extract proper nouns from a text with exceptions and capitalized words that are not proper nouns.
- **Input**: 
  ```python
  text = "This is The Best Day Ever In History."
  ```
- **Expected Output**: 
  ```python
  ["Best", "Day", "Ever", "History"]
  ```

### Test Case 3: Edge Case
- **Scenario**: Extract proper nouns from a text without capitalized words.
- **Input**: 
  ```python
  text = "the quick brown fox jumps over the lazy dog."
  ```
- **Expected Output**: 
  ```python
  []
  ```

---

## 3. Method: `extract_keywords`

### Test Case 1: Standard Case
- **Scenario**: Extract keywords found in the text.
- **Input**: 
  ```python
  text = "Every day, I film scenes for my new project. The crew is always busy."
  keywords = ["film", "project", "busy"]
  ```
- **Expected Output**: 
  ```python
  ["film", "project", "busy"]
  ```

### Test Case 2: Interesting Case
- **Scenario**: Extract keywords from text with repeated keywords.
- **Input**: 
  ```python
  text = "I film scenes for my project. The project is always busy."
  keywords = ["film", "project", "busy"]
  ```
- **Expected Output**: 
  ```python
  ["film", "project", "busy"]
  ```

### Test Case 3: Edge Case
- **Scenario**: Extract keywords when none are found.
- **Input**: 
  ```python
  text = "I read books and write articles."
  keywords = ["film", "project", "busy"]
  ```
- **Expected Output**: 
  ```python
  []
  ```

---

## 4. Method: `tokenize_text`

### Test Case 1: Standard Case
- **Scenario**: Tokenize text with common words.
- **Input**: 
  ```python
  text = "Every day, I film scenes for my new project. The crew is always busy."
  ```
- **Expected Output**: 
  ```python
  ["Every", "day", "I", "film", "scenes", "for", "my", "new", "project", "The", "crew", "is", "always", "busy"]
  ```

### Test Case 2: Interesting Case
- **Scenario**: Tokenize text containing punctuation and numbers.
- **Input**: 
  ```python
  text = "I have $100.50 in my account, but I owe 20% to the bank."
  ```
- **Expected Output**: 
  ```python
  ["I", "have", "100", "50", "in", "my", "account", "but", "I", "owe", "20", "to", "the", "bank"]
  ```

### Test Case 3: Edge Case
- **Scenario**: Tokenize an empty text.
- **Input**: 
  ```python
  text = ""
  ```
- **Expected Output**: 
  ```python
  []
  ```

---

## Test Plan for FST Processing

---

## 1. Method: `transformate_antonyms`

### Test Case 1: Standard Case 
- **Scenario**: Process text with synonyms using the FST.
- **Input**:  
  ```python
  text = "The garden was filled with abundant flowers, their vibrant colors stretching as far as the eye could see."
  ```
- **Expected Output**:  
  ```python
  ["The garden was filled with plentiful flowers, their vibrant colors stretching as far as the eye could see.",
   "The garden was filled with ample flowers, their vibrant colors stretching as far as the eye could see.",
   "The garden was filled with abundant flowers, their vibrant colors stretching as far as the eye could see."]
  ```

### Test Case 2: Limiting Case 
- **Scenario**: Process text with no synonyms.
- **Input**:  
  ```python
  text = "The cat is sleeping."
  ```
- **Expected Output**:  
  ```python
  "The cat is sleeping."
  ```

### Test Case 3: Interesting Case  
- **Scenario**: Process text with multiple synonyms.
- **Input**:  
  ```python
  text = "The beautiful, big garden was abundant with flowers."
  ```
- **Expected Output**:  
  ```python
  ["The attractive, large garden was plentiful with flowers.",
   "The attractive, huge garden was ample with flowers.",
   "The lovely, large garden was abundant with flowers."]
  ```

---

## 2. Method: `transformate_synonyms`

### Test Case 1: Standard Case
- **Scenario**: Process text with antonyms using the FST.
- **Input**:  
  ```python
  text = "The garden was filled with abundant flowers, their vibrant colors stretching as far as the eye could see."
  ```
- **Expected Output**:  
  ```python
  ["The garden was filled with scarce flowers, their vibrant colors stretching as far as the eye could see.",
   "The garden was filled with limited flowers, their vibrant colors stretching as far as the eye could see.",
   "The garden was filled with meager flowers, their vibrant colors stretching as far as the eye could see."]
  ```

### Test Case 2: Limiting Case  
- **Scenario**: Process text with no antonyms.
- **Input**:  
  ```python
  text = "The sky is blue and the sun is shining."
  ```
- **Expected Output**:  
  ```python
  "The sky is blue and the sun is shining."
  ```

### Test Case 3: Interesting Case 
- **Scenario**: Process text with multiple antonyms.
- **Input**:  
  ```python
  text = "The angry gardener had an abundant supply of seeds."
  ```
- **Expected Output**:  
  ```python
  ["The calm gardener had a scarce supply of seeds.",
   "The peaceful gardener had a limited supply of seeds.",
   "The happy gardener had a meager supply of seeds."]
  ```

---

## 3. Method: `create_fst_present_to_future_simple`

### Test Case 1: Standard Case  
- **Scenario**: Convert present tense to future tense.
- **Input**:  
  ```python
  text = "She dances gracefully and they are always amazed by her performance."
  ```
- **Expected Output**:  
  ```python
  "She will dance gracefully and they will be always amazed by her performance."
  ```

### Test Case 2: Limiting Case
- **Scenario**: Process text with no future tense changes.
- **Input**:  
  ```python
  text = "The cat ventures on the couch every day."
  ```
- **Expected Output**:  
  ```python
  "The cat ventures on the couch every day."
  ```

### Test Case 3: Interesting Case
- **Scenario**: Convert multiple sentences to future tense.
- **Input**:  
  ```python
  text = "Every day, I film scenes for my new project."
  ```
- **Expected Output**:  
  ```python
  "Every day, I will film scenes for my new project."
  ```

---

## 4. Method: `create_fst_present_to_past_simple`

### Test Case 1: Present to Past Simple Case  
- **Scenario**: Convert present tense to past tense.
- **Input**:  
  ```python
  text = "I am dancing while they are watching."
  ```
- **Expected Output**:  
  ```python
  "I was dancing while they were watching."
  ```

### Test Case 2: Limiting Case 
- **Scenario**: Process text with no past tense changes.
- **Input**:  
  ```python
  text = "The dog barks at the mailman."
  ```
- **Expected Output**:  
  ```python
  "The dog barks at the mailman."
  ```

### Test Case 3: Interesting Case 
- **Scenario**: Convert a longer text with multiple sentences to past tense.
- **Input**:  
  ```python
  current_text1 = """Every day, I film scenes for my new project. The crew is always busy, and we are filming from early morning until late at night."""
  ```
- **Expected Output**:  
  ```python
  "Every day, I filmed scenes for my new project. The crew was always busy, and we were filming from early morning until late at night."
  ```

---

## 5. Method: `create_fst_present_to_continuous`

### Test Case 1: Standard Case
- **Objective:** To check if the FST correctly transforms present simple tenses into present continuous in a standard case.
- **Input:** `"Every day, I work and she admires the beauty."`
- **Expected Output:** `"Every day, I am working and she is admiring the beauty."`
- **Pass Criteria:** The output must transform both verbs to present continuous.

### Test Case 2: Limiting Case
- **Objective:** To verify if the FST leaves the sentence unchanged when no verbs need transformation.
- **Input:** `"The weather feels vibrant today."`
- **Expected Output:** `"The weather feels vibrant today."`
- **Pass Criteria:** The output should be identical to the input since no transformation is required.

### Test Case 3: Interesting Case
- **Objective:** To assess how the FST handles a more complex text with multiple verb transformations.
- **Input:** `current_text1`
- **Expected Output:** A text where all applicable verbs are correctly transformed into present continuous tense.
- **Pass Criteria:** All present simple verbs should be transformed into present continuous while maintaining grammatical accuracy.

---

## 6. Method: `create_fst_pronouns_to_i`

### Test Case 1: Standard Case
- **Objective:** To verify that the pronoun "I" replaces third-person pronouns ("he", "she") in a standard sentence.
- **Input:** `"He is going to the store, and she is buying groceries."`
- **Expected Output:** `"I am going to the store, and I am buying groceries."`
- **Pass Criteria:** Both third-person pronouns should be replaced with "I" and verbs adjusted accordingly.

### Test Case 2: Limiting Case
- **Objective:** To check if no changes occur when the input sentence does not contain third-person pronouns.
- **Input:** `"They are going to the store."`
- **Expected Output:** `"They are going to the store."`
- **Pass Criteria:** The output should remain unchanged as there is no need for transformation.

### Test Case 3: Interesting Case
- **Objective:** To ensure that the transformation applies accurately to a longer and more complex text.
- **Input:** `current_text1`
- **Expected Output:** A version of the text where all applicable pronouns are changed to "I" with corresponding verb forms adjusted.
- **Pass Criteria:** The pronouns and verbs should be correctly replaced and conjugated, maintaining coherence throughout the text.

---

## 7. Method: `create_fst_pronouns_to_he`

### Test Case 1: Standard Case
- **Objective:** To check if the pronoun "He" replaces "she" and adjusts verbs accordingly.
- **Input:** `"She is handling the camera, while I am adjusting the settings."`
- **Expected Output:** `"He is handling the camera, while he is adjusting the settings."`
- **Pass Criteria:** The pronouns and verbs should correctly reflect the change from "she" to "he."

### Test Case 2: Limiting Case
- **Objective:** To check if the transformation applies to minimal text.
- **Input:** `"I am"`
- **Expected Output:** `"He is"`
- **Pass Criteria:** The transformation should correctly replace "I" with "he" and adjust the verb.

### Test Case 3: Interesting Case
- **Objective:** To assess the transformation in a longer text.
- **Input:** `current_text1`
- **Expected Output:** A text where all "I" and "she" are replaced with "he" and verbs adjusted accordingly.
- **Pass Criteria:** All pronouns should be replaced, and the verb forms must be correct.

---

## 8. Method: `create_fst_pronouns_to_she`

### Test Case 1: Standard Case
- **Objective:** To check if the pronoun "she" replaces other pronouns and adjusts verbs accordingly.
- **Input:** `current_text1`
- **Expected Output:** A text where "I" and "he" are replaced by "she."
- **Pass Criteria:** The transformation must correctly replace the pronouns and adjust verb forms.

### Test Case 2: Limiting Case
- **Objective:** To verify if the transformation occurs in a minimal text.
- **Input:** `"I am"`
- **Expected Output:** `"She is"`
- **Pass Criteria:** The pronoun "I" should be replaced with "she" and the verb correctly conjugated.

### Test Case 3: Interesting Case
- **Objective:** To test the transformation on a more complex sentence structure.
- **Input:** `"He is handling the camera, while I am adjusting the settings. It is fascinating to see how it works."`
- **Expected Output:** `"He is handling the camera, while she is adjusting the settings. She is fascinating to sees how she works."`
- **Pass Criteria:** All relevant pronouns and verbs should be transformed and conjugated correctly.

---

## 9. Method: `create_fst_pronouns_to_it`

### Test Case 1: Standard Case
- **Objective:** To verify that the pronoun "it" is applied correctly in a larger text.
- **Input:** `current_text1`
- **Expected Output:** A text where "I," "he," and "she" are replaced with "it."
- **Pass Criteria:** The pronouns and verb forms should reflect the correct transformation.

### Test Case 2: Limiting Case
- **Objective:** To check if the transformation occurs with minimal input.
- **Input:** `"I am"`
- **Expected Output:** `"It is"`
- **Pass Criteria:** The transformation should apply correctly.

### Test Case 3: Interesting Case
- **Objective:** To test the transformation in a complex sentence.
- **Input:** `"She is handling the camera, and he is adjusting the lights. I am watching."`
- **Expected Output:** `"It is handling the camera, and he is adjusting the lights. It is watching."`
- **Pass Criteria:** All pronouns should be replaced with "it," and the verb forms must be accurate.

---

## 10. Method:  `create_fst_pronouns_to_it`

### Test Case 1: Standard Case
- **Objective:** To check if "they" replaces "we" in a standard sentence.
- **Input:** `"We are going to the store, and we will buy groceries."`
- **Expected Output:** `"They are going to the store, and they will buy groceries."`
- **Pass Criteria:** The pronouns and verbs should correctly reflect the change from "we" to "they."

### Test Case 2: Limiting Case
- **Objective:** To check if no transformation occurs in a sentence with different pronouns.
- **Input:** `"He is going to the store."`
- **Expected Output:** `"He is going to the store."`
- **Pass Criteria:** The sentence should remain unchanged as "they" transformation is not applicable.

### Test Case 3: Interesting Case
- **Objective:** To assess how "they" is applied to a more complex text.
- **Input:** `self.current_text1`
- **Expected Output:** A text where "we" is replaced with "they," and verbs are conjugated correctly.
- **Pass Criteria:** All pronouns should be replaced, and verb forms must be correctly adjusted.

---

## 11. Method:  `create_fst_pronouns_to_we`

### Test Case 1: Standard Case
- **Objective:** To verify if "they" is correctly replaced by "we" in a standard sentence.
- **Input:** `"They are going to the store, and they will buy groceries."`
- **Expected Output:** `"We are going to the store, and we will buy groceries."`
- **Pass Criteria:** All occurrences of "they" should be changed to "we".

### Test Case 2: Limiting Case
- **Objective:** To check that no transformation occurs in a sentence with different pronouns.
- **Input:** `"She is going to the store."`
- **Expected Output:** `"She is going to the store."`
- **Pass Criteria:** The sentence should remain unchanged, as "they" transformation is not applicable.

### Test Case 3: Interesting Case
- **Objective:** To assess how "we" is applied to a more complex text.
- **Input:** `self.current_text1`
- **Expected Output:** A text where "they" is replaced with "we," and verbs are conjugated correctly.
- **Pass Criteria:** All pronouns should be replaced, and verb forms must be correctly adjusted.

---

## 12. Method:  `create_fst_pronouns_to_they`

### Test Case 1: Standard Case
- **Objective:** To verify if "we" is correctly replaced by "they" in a standard sentence.
- **Input:** `"We are going to the store, and we will buy groceries."`
- **Expected Output:** `"They are going to the store, and they will buy groceries."`
- **Pass Criteria:** All occurrences of "we" should be changed to "they".

### Test Case 2: Limiting Case
- **Objective:** To check that no transformation occurs in a sentence with different pronouns.
- **Input:** `"He is going to the store."`
- **Expected Output:** `"He is going to the store."`
- **Pass Criteria:** The sentence should remain unchanged, as "we" transformation is not applicable.

### Test Case 3: Interesting Case
- **Objective:** To assess how "they" is applied to a more complex text.
- **Input:** `self.current_text1`
- **Expected Output:** A text where "we" is replaced with "they," and verbs are conjugated correctly.
- **Pass Criteria:** All pronouns should be replaced, and verb forms must be correctly adjusted.

---



## Test Plan for CFG

---

## 1. Method: `get_sentences`

### Test Case 1: Standard Case
- **Objective:** Verify that the `get_sentences` method can correctly split a text into sentences while removing punctuation.
- **Input:** 
  ```python
  "I went to the market, and I bought some fruits."
  ```
- **Expected Output:**
  ```python
  ["I went to the market", "and I bought some fruits"]
  ```
- **Pass Criteria:** The method should return a list of two sentences, properly separating by punctuation and removing extra spaces.

### Test Case 2: Limiting Case
- **Objective:** Check the method's behavior when there are no punctuation marks to separate the sentences.
- **Input:** 
  ```python
  "He plays football every day"
  ```
- **Expected Output:**
  ```python
  ["He plays football every day"]
  ```
- **Pass Criteria:** The method should return a list with a single sentence since there is no punctuation.

### Test Case 3: Interesting Case
- **Objective:** Evaluate the method's behavior with multiple sentences and different punctuation marks.
- **Input:** 
  ```python
  "I am happy! She is running; They were sleeping, but now they are awake."
  ```
- **Expected Output:**
  ```python
  ["I am happy", "She is running", "They were sleeping", "but now they are awake"]
  ```
- **Pass Criteria:** The method should correctly separate sentences according to various punctuation marks.

---

## 2. Method: `create_cfg`

### Test Case 1: Unique Case
- **Objective:** Verify that the `create_cfg` method correctly generates a CFG with the expected productions for sentences in present simple and past simple.
- **Input:** Nothing
- **Expected Output:** A valid CFG that can recognize a sentence
- **Pass Criteria:** The CFG should contain productions that allow the generation of sentences with a noun and a verb.

---

## 3. Method: `analyze_sentence`

### Test Case 1: Standard Case  
- **Scenario**: Validate a complete sentence in the present simple tense.
- **Input**:  
  ```python
  sentence = "The cat sits on the mat."
  ```
- **Expected Output**:  
  ```python
  is_valid = True
  ```

### Test Case 2: Limiting Case  
- **Scenario**: Validate an incomplete sentence missing a verb.
- **Input**:  
  ```python
  sentence = "The cat."
  ```
- **Expected Output**:  
  ```python
  is_valid = False
  ```

### Test Case 3: Interesting Case  
- **Scenario**: Validate a sentence with a past tense verb to ensure it processes correctly.
- **Input**:  
  ```python
  sentence = "She ran to store"
  ```
- **Expected Output**:  
  ```python
  is_valid = True
  ```

---

## 4. Method: `validate`

### Test Case 1: Standard Case
- **Objective:** Verify that the `validate` method recognizes sentences in the present simple tense.
- **Input:** 
  ```plaintext
  "They love me. The dog barked. She reads a book. He plays football."
  ```
- **Expected Output:**
```plaintext
[["They love me", True, [('They', 'PRP'), ('love', 'VBP'), ('me', 'PRP')]], 
 ["The dog barked", True, [('The', 'DT'), ('dog', 'NN'), ('barked', 'VBD')]], 
 ["She reads a book.", True, [('She', 'PRP'), ('reads', 'VBZ'), ('a', 'DT'), ('book', 'NN')]], 
 ["He plays football.", True, [('He', 'PRP'), ('plays', 'VBZ'), ('football', 'NN')]]]
 ```
- **Pass Criteria:** The method should return a list containing each sentence, a boolean value indicating that it is valid, and a list of tuples with the words and their part-of-speech tags..

---

### Test Case 2: Limiting Case
- **Objective:** Check how the `validate` method handles incomplete sentences or sentences without a verb.
- **Input:** 
  ```plaintext
  "The cat. The dog barks run and the. She he it now."
  ```
- **Expected Output:**
```plaintext
[["The cat.", False, [('The', 'DT'), ('cat', 'NN')]], 
 ["The dog barks run and the.", False, [('The', 'DT'), ('dog', 'NN'), (barks, 'NNS'), (run, 'VBP'), (and, 'CC'), (the, 'DT')]],
 ["She he it now.", False, [('She', 'PRP'), (he, 'PRP'), (it, 'PRP'), (now, 'RB')]]]
 ```
- **Pass Criteria:** The method should return a list containing each sentence, a boolean value indicating that the sentence is invalid, and a list of tuples with the words and their part-of-speech tags.

---

### Test Case 3: Interesting Case
- **Objective:** Test how the `validate` method handles complex sentences in the past simple tense.
- **Input:** 
  ```plaintext
  "The cat ran, the dog barked. She finished homework. They played soccer."
  ```
- **Expected Output:**
```plaintext
  [["The cat ran.", True, [('The', 'DT'), ('cat', 'NN'), ('ran', 'VBD')]], 
 ["The dog barked.", True, [('the', 'DT'), ('dog', 'NN'), ('barked', 'VBD')]], 
 ["She finished homework.", True, [('She', 'PRP'), ('finished', 'VBD'), ('homework', 'NN')]], 
 ["They played soccer.", True, [('They', 'PRP'), ('played', 'VBD'), ('soccer', 'NN')]]]
  ```
- **Pass Criteria:** The method should return a list containing each sentence, a boolean value indicating that it is valid, and a list of tuples with the words and their part-of-speech tags.

---

## Test Plan for Text Transformation UI

### Test Case 1: Standard Input Transformation
- **Scenario**: Transform standard input text from present tense to past tense.
- **Input**: 
  ```
  "Every day, I film scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all work together, and each person plays a vital role. He is handling the camera, while she is adjusting the lights. They are financing the project, ensuring we have enough funds to continue. I am careful when I film, trying to capture every detail. Sometimes, I fire questions at the actors to help them understand the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we work together to fix them."
  ```
- **Expected Output**: 
  ```
  "Every day, I filmed scenes for my new project. The crew was always busy, and we were filming from early morning until late at night. We all worked together, and each person played a vital role. He was handling the camera, while she was adjusting the lights. They were financing the project, ensuring we have enough funds to continue. I was careful when I filmed, trying to capture every detail. Sometimes, I fired questions at the actors to help them understand the scene better. The script was already fixed, but we were always open to making small changes. When problems arose, we worked together to fix them."
  ```

### Test Case 2: Empty Input Handling
- **Scenario**: Handle an empty input string.
- **Input**: 
  ```
  ""
  ```
- **Expected Output**: 
  ```
  "Input cannot be empty. Please enter text to transform."
  ```

### Test Case 3: Unrelated Tense
- **Scenario**: Input text that is already in past tense.
- **Input**: 
  ```
  "I filmed the scene yesterday."
  ```
- **Expected Output**: 
  ```
  "I filmed the scene yesterday."
  ```

---

## Test Plan for Text Summarization UI

### Test Case 1: Standard Input Summarization
- **Scenario**: Summarize standard input text using the provided keywords.
- **Input**: 
  ```plaintext
  "Every day, I film scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. We all work together, and each person plays a vital role. He is handling the camera, while she is adjusting the lights. They are financing the project, ensuring we have enough funds to continue. I am careful when I film, trying to capture every detail. Sometimes, I fire questions at the actors to help them understand the scene better. The script is already fixed, but we are always open to making small changes. When problems arise, we work together to fix them."
  ```
- **Keywords**: 
  ```plaintext
  crew, camera
  ```
- **Expected Output**: 
  ```plaintext
  "Every day, I film scenes for my new project. The crew is always busy, and we are filming from early morning until late at night. He is handling the camera, while she is adjusting the lights. I am careful when I film, trying to capture every detail. Sometimes, I fire questions at the actors to help them understand the scene better."
  ```

### Test Case 2: Input Validation
- **Scenario**: Input text that is empty.
- **Input**: 
  ```plaintext
  ""
  ```
- **Keywords**: 
  ```plaintext
  crew, camera
  ```
- **Expected Output**: 
  ```plaintext
  ""
  ```

### Test Case 3: Keyword Handling
- **Scenario**: Input text without any of the specified keywords.
- **Input**: 
  ```plaintext
  "I enjoy filmmaking and learning new techniques."
  ```
- **Keywords**: 
  ```plaintext
  crew, camera
  ```
- **Expected Output**: 
  ```plaintext
  ""
  ```

--- 

## Test Plan for Text Validation UI

### Test Case 1: Standard Input Transformation
- **Scenario**: Validate standard input text that is in present simple and in past simple.
- **Input**: 
  ```
  "The sun shines in the sky. Birds sing in the trees. John wakes up early every morning. He drinks his coffee and reads the newspaper. Then, he goes for a walk in the park. Flowers bloom and the air is fresh. Children play on the grass. Yesterday, John decided to visit his friend. He went to his house and they played music together. They ate pizza and laughed a lot. Afterward, they watched a movie. John felt happy to spend time with him."
  ```
- **Expected Output**: 
  ```
  "1. The sun shines in the sky: false | Tagging: The,DT,sun,NN,shines,NNS,in,IN,the,DT,sky,NN
  2. Birds sing in the trees: true | Tagging: Birds,NNS,sing,VBG,in,IN,the,DT,trees,NNS
  3. John wakes up early every morning: false | Tagging: John,NNP,wakes,VBZ,up,RP,early,JJ,every,DT,morning,NN
  4. He drinks his coffee and reads the newspaper: false | Tagging: He,PRP,drinks,VBZ,his,PRP$,coffee,NN,and,CC,reads,VBZ,the,DT,newspaper,NN
  5. Then: false | Tagging: Then,RB
  6. he goes for a walk in the park: true | Tagging: he,PRP,goes,VBZ,for,IN,a,DT,walk,NN,in,IN,the,DT,park,NN
  7. Flowers bloom and the air is fresh: false | Tagging: Flowers,NNS,bloom,NN,and,CC,the,DT,air,NN,is,VBZ,fresh,JJ
  8. Children play on the grass: false | Tagging: Children,NNP,play,NN,on,IN,the,DT,grass,NN
  9. Yesterday: false | Tagging: Yesterday,NN
  10. John decided to visit his friend: true | Tagging: John,NNP,decided,VBD,to,TO,visit,VB,his,PRP$,friend,NN
  11. He went to his house and they played music together: false | Tagging: He,PRP,went,VBD,to,TO,his,PRP$,house,NN,and,CC,they,PRP,played,VBD,music,NN,together,RB
  12. They ate pizza and laughed a lot: false | Tagging: They,PRP,ate,VBP,pizza,NN,and,CC,laughed,VBD,a,DT,lot,NN
  13. Afterward: false | Tagging: Afterward,RB
  14. they watched a movie: true | Tagging: they,PRP,watched,VBD,a,DT,movie,NN
  15. John felt happy to spend time with him: false | Tagging: John,NNP,felt,VBD,happy,JJ,to,TO,spend,VB,time,NN,with,IN,him,PRP"
  ```

### Test Case 2: Empty Input Handling
- **Scenario**: Handle an empty input string.
- **Input**: 
  ```
  ""
  ```
- **Expected Output**: 
  ```
  ""
  ```

### Test Case 3: No Sense Sentences
- **Scenario**: Input text that has no sense.
- **Input**: 
  ```
  "The DiscretasIII. So many responses in and the book gather. I love love to love and be so fruit loved and Mariana computer."
  ```
- **Expected Output**: 
  ```
  "1. The DiscretasIII: false | Tagging: The,DT,DiscretasIII,NNP
  2. So many responses in and the book gather: false | Tagging: So,RB,many,JJ,responses,NNS,in,IN,and,CC,the,DT,book,NN,gather,NN
  3. I love love to love and be so fruit loved and Mariana computer: false | Tagging: I,PRP,love,VBP,love,VB,to,TO,love,VB,and,CC,be,VB,so,RB,fruit,JJ,loved,VBN,and,CC,Mariana,NNP,computer,NN"
