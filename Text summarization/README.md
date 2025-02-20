![ICESI University Logo](https://www.icesi.edu.co/launiversidad/images/La_universidad/logo_icesi.png)

# Computing and Discrete Structures III - Software Engineering

# Text Summarization and Transformation System

## Team members

- Dylan Bermúdez Cardona
- Juan David Calderón Salamanca
- Santiago Escobar León

## Overview

The Text Summarization and Transformation System is designed to process textual input, generate concise summaries, and transform these summaries based on user-defined rules. The system leverages various elements of formal language theory, including regular expressions, finite automata (FA), finite state transducers (FST), and context-free grammars (CFGs), to parse, analyze, and manipulate text.

> [!NOTE]
> *Reference: Bird, Steven, Edward Loper and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.*

## Step-by-Step Program Outline

1. **Text Preprocessing and Tokenization (Regular Expressions)**:
   - **Objective**: Clean and preprocess the input text by identifying sentences, keywords, and other relevant components.
   - **Implementation**: Use Python's `re` module to define regular expressions for splitting the text into sentences, identifying proper nouns, and extracting keywords.

2. **Text Summarization (Finite Automata)**:
   - **Objective**: Select key sentences that summarize the input text based on the presence of keywords, sentence structure, and other heuristics.
   - **Implementation**: Create a FA using `pyformlang` that traverses the tokenized text and identifies sentences that match certain patterns.

3. **Text Transformation (Finite State Transducers)**:
   - **Objective**: Apply user-defined transformations to the summarized text.
   - **Implementation**: Use `pyformlang` to create an FST that maps the original summary to a transformed version according to specific rules.

    ### Restrictions FST:
   - **Verb Tenses**: The input is assumed to be in **simple present tense**. The transformation allows changing from simple present to **simple past**, **present continuous**, or **simple future**. However, once transformed, there is no way to revert to previous tenses.
   - **Pronoun Changes**: The transducer only supports changes for **subject pronouns** (e.g., "I", "he", "she", "they"), and transformations apply solely to these types of pronouns.
   - **Limited Vocabulary**: Synonyms, antonyms, and verbs are restricted to a pre-defined **dictionary** created by the team, meaning transformations are limited to the words and structures available within that dictionary.


4. **Grammar Validation (Context-Free Grammar)**:
   - **Objective**: Ensure that the transformed summary is grammatically correct and maintains the intended meaning.
   - **Implementation**: Define a CFG using `pyformlang` to validate the structure of the transformed summary.

   ### Restrictions CFG:
   Our CFG verifies:
   - **Basic Subject-Verb-Object (SVO) Structure:** The CFG verifies that sentences follow this common English structure, where a noun phrase (NP) is followed by a verb phrase (VP).
   - **Phrase Combinations:** It handles sentences that include prepositional, adjectival, and adverbial phrases, which modify nouns or verbs.
   - **Sentence Coordination:** The CFG supports coordination of sentences using conjunctions, allowing structures like "S1 CONJ S2", where both follow the    basic SVO format.
   - **Modified Phrases:** It permits the addition of modifiers, like adjectives for nouns and adverbs for verbs, adding flexibility to noun and verb phrases.

   But, we have limitations:
   - We are working with a limited structure due to the vast number of potential sentence combinations in English. The CFG is designed to handle a restricted set of simple sentences, and it fails to cover more complex linguistic phenomena such as:
   - Due to the nature of the NLTK library, some words might not be recognized correctly based on their semantic meaning in a given sentence. As a result, unexpected errors can occur.


## Related links
- [Poster](https://www.figma.com/design/Vqs2k3NjgoiU8KWNPFUBlH/Untitled?node-id=0-1&t=Qj3pgjxU3rkAnhtJ-1)
- [Test plan](https://github.com/Bloque-CED/integrative-task-1-grupo-niche/blob/main/doc/Test_plan.md)
  
## Requirements

To install the required packages, run:

```bash
pip install -r requirements.txt
```

The ```requirements.txt``` file should contain:

```bash
pyformlang==1.0.10
coverage==7.6.1
fastapi[all]
uvicorn==0.31.0
nltk==3.9.1
```

To run the backend, navigate to the backend directory and execute:

```bash
integrative-task-1-grupo-niche\src\backend> python -m uvicorn app:app --reload
```

To run the frontend, navigate to the frontend directory and execute:

```bash
integrative-task-1-grupo-niche\src\frontend\summarizer> npm run dev
```

### **Developed with** 🛠️

<div style="text-align: left">
    <p>
        <a href="https://code.visualstudio.com/" target="_blank"> <img alt="Visual Studio Code" src="https://cdn.svgporn.com/logos/visual-studio-code.svg" height="60" width = "60"></a>
    </p>
</div>
