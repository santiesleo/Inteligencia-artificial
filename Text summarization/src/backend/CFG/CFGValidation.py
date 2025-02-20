import nltk
import re
from nltk import word_tokenize, pos_tag
from pyformlang.cfg import Variable, Terminal, Production, CFG

# Descargar recursos necesarios de NLTK
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

cfg = None

def validate(text):
    global cfg
    validated = []
    sentences = get_sentences(text)

    if cfg is None:
        cfg = create_cfg()

    for s in sentences:
        v, tag = analyze_sentence(s, cfg)
        validated.append([s, v, tag])
    
    return validated

def get_sentences(text):
    pattern = re.compile(r'[^.,:;!]+')
    sentences = pattern.findall(text)
    clean_sentences = [s.strip() for s in sentences]
    return clean_sentences

def create_cfg():
    # Variables
    S = Variable("S")
    NP = Variable("NP")
    VP = Variable("VP")
    PP = Variable("PP")
    ADJP = Variable("ADJP")
    ADVP = Variable("ADVP")
    
    # Terminales
    NOUN = Terminal("NOUN")
    PRONOUN = Terminal("PRONOUN")
    VERB = Terminal("VERB")
    AUX = Terminal("AUX")
    DET = Terminal("DET")
    ADJ = Terminal("ADJ")
    ADV = Terminal("ADV")
    PREP = Terminal("PREP")
    CONJ = Terminal("CONJ")
    TO = Terminal("TO")
    
    # Producciones
    productions = [
        Production(S, [NP, VP]),
        Production(S, [S, CONJ, S]),
        Production(NP, [DET, NOUN]),
        Production(NP, [DET, ADJP, NOUN]),
        Production(NP, [NOUN]),
        Production(NP, [PRONOUN]),
        Production(NP, [NP, PP]),
        Production(NP, [ADJ, NOUN]),
        Production(NP, [DET, NP]),
        Production(VP, [VERB]),
        Production(VP, [VERB, NP]),
        Production(VP, [VERB, NP, PP]),
        Production(VP, [VERB, PP]),
        Production(VP, [VP, ADVP]),
        Production(VP, [ADVP, VP]),
        Production(VP, [AUX, VP]),
        Production(VP, [AUX, VERB]),
        Production(VP, [AUX, VERB, NP]),
        Production(VP, [VERB, TO, VP]),
        Production(VP, [AUX, VERB, VP]),  # Para manejar formas continuas
        Production(PP, [PREP, NP]),
        Production(ADJP, [ADJ]),
        Production(ADJP, [ADJ, ADJP]),
        Production(ADVP, [ADV]),
        Production(ADVP, [ADV, ADVP])
    ]
    
    return CFG(variables={S, NP, VP, PP, ADJP, ADVP},
               terminals={NOUN, PRONOUN, VERB, AUX, DET, ADJ, ADV, PREP, CONJ, TO},
               start_symbol=S,
               productions=productions)

def analyze_sentence(sentence, cfg):
    tokens = word_tokenize(sentence)
    tagged = pos_tag(tokens)
    
    cfg_tokens = []
    for word, tag in tagged:
        if tag.startswith('N'):
            cfg_tokens.append(Terminal("NOUN"))
        elif tag.startswith('V'):
            if tag in ['VB', 'VBP', 'VBZ', 'VBD', 'VBN']:
                cfg_tokens.append(Terminal("VERB"))
            elif tag == 'VBG':
                cfg_tokens.append(Terminal("VERB"))
            elif tag == 'MD':
                cfg_tokens.append(Terminal("AUX"))
        elif tag in ['DT', 'PRP$']:
            cfg_tokens.append(Terminal("DET"))
        elif tag == 'PRP':
            cfg_tokens.append(Terminal("PRONOUN"))
        elif tag.startswith('JJ'):
            cfg_tokens.append(Terminal("ADJ"))
        elif tag.startswith('RB'):
            cfg_tokens.append(Terminal("ADV"))
        elif tag == 'IN':
            cfg_tokens.append(Terminal("PREP"))
        elif tag == 'CC':
            cfg_tokens.append(Terminal("CONJ"))
        elif tag == 'TO':
            cfg_tokens.append(Terminal("TO"))
        else:
            cfg_tokens.append(Terminal("NOUN"))
    
    is_valid = cfg.contains(cfg_tokens)
    
    return is_valid, tagged