from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from FST.FstController import process_text_with_fst
from FST.FstSynonyms import transformate_synonyms
from FST.FstAntonyms import transformate_antonyms
from FST.FstPronouns import *
from FST.FstPastTenses import *
from FST.FstFutureTenses import *
from FST.FstPresentTenses import *
from text_summarization.DFASummarizer import DFASummarizer
from text_processing.Preprocessor import Preprocessor
from CFG.CFGValidation import *

app = FastAPI()

# Habilitar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

# Input and output schemas
class TextProcessingRequest(BaseModel):
    text: str

class FSTRequest(BaseModel):
    fst_option: str
    input_string: str

class DFARequest(BaseModel):
    keywords: list
    dfa_input: str

class CFGRequest(BaseModel):
    cfg_string: str

# /text-processing endpoint
@app.post("/text-processing")
async def text_processing(request: TextProcessingRequest):
    text = request.text
    # Simple example: convert text to uppercase and count words
    processed_text = text.upper()
    word_count = len(text.split())
    return {"processed_text": processed_text, "word_count": word_count}

# /FST endpoint
@app.post("/FST")
async def fst_endpoint(request: FSTRequest):
    # Selección del FST en función de la opción proporcionada
    fst = None
    if request.fst_option == "Change verb tenses (simple present to simple past)":
        fst = create_fst_present_to_past_simple()
    #TODO: ELIMINAR DEL FRONTEND ESTA FUNCIONALIDAD
    elif request.fst_option == "Change verb tenses (simple past to simple present)":
        pass
        #fst = create_fst_past_simple_to_present_simple() 
    #TODO: ELIMINAR DEL FRONTEND ESTA FUNCIONALIDAD
    elif request.fst_option == "Change verb tenses (simple present to simple future)":
        fst = create_fst_present_to_future_simple()
    elif request.fst_option == "Change verb tenses (simple present to present continuous)":
        fst = create_fst_present_to_continuous()
    elif request.fst_option == "Change pronouns to 'I'":
        fst = create_fst_pronouns_to_i()
    elif request.fst_option == "Change pronouns to 'you'":
        fst = create_fst_pronouns_to_you()
    elif request.fst_option == "Change pronouns to 'he'":
        fst = create_fst_pronouns_to_he()
    elif request.fst_option == "Change pronouns to 'she'":
        fst = create_fst_pronouns_to_she()
    elif request.fst_option == "Change pronouns to 'it'":
        fst = create_fst_pronouns_to_it()
    elif request.fst_option == "Change pronouns to 'we'":
        fst = create_fst_pronouns_to_we()
    elif request.fst_option == "Change pronouns to 'they'":
        fst = create_fst_pronouns_to_they()
    elif request.fst_option == "Apply synonyms":
        fst = transformate_synonyms()
    elif request.fst_option == "Apply antonyms":
        fst = transformate_antonyms()
    else:
        raise HTTPException(status_code=400, detail="Invalid FST option")

    # Procesar el texto con el FST seleccionado
    output_string = process_text_with_fst(fst, request.input_string)
    return {"input_string": request.input_string, "fst_output": output_string}

# /DFA-summarizer endpoint
@app.post("/DFA-summarizer")
async def dfa_summarizer(request: DFARequest):
    keywords = request.keywords
    dfa_input = request.dfa_input
    
    prep = Preprocessor()
    sentences = prep.split_sentences(dfa_input)
    
    # pasar a minúsculas la primera palabra de cada oración
    sentences_lowercase = [sentence[0].lower() + sentence[1:] if sentence else sentence for sentence in sentences]

    # nouns y keywords
    proper_nouns = prep.extract_proper_nouns(dfa_input)
    combined_keywords = prep.extract_keywords(dfa_input, keywords + proper_nouns)
    print(sentences_lowercase)
    
    # instancia del DFASummarizer con las palabras clave proporcionadas
    dfa_summarizer = DFASummarizer(combined_keywords)
    
    # Resumir el texto utilizando el DFA
    summary = dfa_summarizer.summarize_text(sentences_lowercase)
    
    # Devolver el resultado como JSON
    return {"dfa_input": dfa_input, "dfa_summary": summary}

# /CFG-validation endpoint
@app.post("/CFG-validation")
async def cfg_validation(request: CFGRequest):
    cfg_string = request.cfg_string

    validated = validate(cfg_string)

    return {"cfg_string": cfg_string, "cfg_validation": validated}

# Running the API
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
