'use client';

import React, { useState } from 'react';
import axios from 'axios';

const SummarizerPage = () => {
  const [inputText, setInputText] = useState('');
  const [outputText, setOutputText] = useState('');
  const [activeOption, setActiveOption] = useState('');
  const [TransformationOption, setTransformationOption] = useState('');
  const [keywords, setKeywords] = useState<string[]>([]); // Array para manejar las keywords
  const [newKeyword, setNewKeyword] = useState(''); // Manejar el input de la nueva keyword

  const TransformationOptions = [
    "Change verb tenses (simple present to simple past)",
    "Change verb tenses (simple past to simple present)",
    "Change verb tenses (simple present to simple future)",
    "Change verb tenses (simple present to present continuous)",
    "Change pronouns to 'I'",
    "Change pronouns to 'you'",
    "Change pronouns to 'he'",
    "Change pronouns to 'she'",
    "Change pronouns to 'it'",
    "Change pronouns to 'we'",
    "Change pronouns to 'they'",
    "Apply synonyms",
    "Apply antonyms"
  ];

  const handleSubmit = async (option: string) => {
    try {
      if (activeOption === 'Transformation') {
        const response = await axios.post('http://localhost:8000/FST', {
          fst_option: TransformationOption,
          input_string: inputText,
        });
        setOutputText(response.data.fst_output);
      } else if (activeOption === 'Summarize') {
        const response = await axios.post('http://localhost:8000/DFA-summarizer', {
          keywords: keywords, // Enviar las keywords como parte de la solicitud
          dfa_input: inputText,
        });
        setOutputText(response.data.dfa_summary);
      } else {
        const response = await axios.post('http://localhost:8000/CFG-validation', {
          cfg_string: inputText,
        });

        let str = ''
        console.log(response)
        const sentences = response.data.cfg_validation

        for (let i = 0; i < sentences.length; i++) {
          str += (i+1) + '. ' + sentences[i][0] + ": " + sentences[i][1] + ' | ' + 'Tagging: ' + sentences[i][2] + '\n'
        }

        setOutputText(str);
      }
    } catch (error) {
      console.error('Error:', error);
      setOutputText('An error occurred. Please try again.');
    }
  };

  // Función para añadir una keyword al array
  const handleAddKeyword = () => {
    if (newKeyword.trim()) {
      setKeywords([...keywords, newKeyword]);
      setNewKeyword(''); // Limpiar el input después de añadir
    }
  };

  // Función para eliminar una keyword del array
  const handleRemoveKeyword = (index: number) => {
    const updatedKeywords = keywords.filter((_, i) => i !== index);
    setKeywords(updatedKeywords);
  };

  const handleOption = (option: any) => {
    setActiveOption(option)
    setOutputText('')
  }

  return (
    <div className="min-h-screen bg-gradient-to-br p-8">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-center text-[#00158E] mb-4">
          Welcome to the Trusted Summarizer
        </h1>
        <p className="text-lg text-center text-black font-regular mb-8">
          A summarizer utilizing FST (Finite State Transducers), DFA (Deterministic Finite Automata), and CFG (Context-Free Grammars).
        </p>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          {['Transformation', 'Summarize', 'Validate'].map((option) => (
            <button
              key={option}
              className={`py-3 px-6 rounded-lg text-white font-semibold transition-colors ${
                activeOption === option
                  ? 'bg-[#00158E] hover:bg-[#000F63]'
                  : 'bg-[#3F5CFF] hover:bg-[#2544F1]'
              }`}
              onClick={() => handleOption(option)}
            >
              {option} Text
            </button>
          ))}
        </div>

        {activeOption && (
          <div className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-2xl font-semibold text-[#00158E] mb-4">
              {activeOption} Text
            </h2>

            {activeOption === 'Transformation' && (
              <select
                className="w-full p-2 mb-4 border border-gray-300 rounded-md text-gray-400"
                value={TransformationOption}
                onChange={(e) => setTransformationOption(e.target.value)}
              >
                <option value="" >Select a translation option</option>
                {TransformationOptions.map((option, index) => (
                  <option key={index} value={option}>
                    {option}
                  </option>
                ))}
              </select>
            )}

            {activeOption === 'Summarize' && (
              <>
                <div className="flex gap-4 mb-4">
                  <input
                    className="flex-1 p-2 border border-gray-300 rounded-md text-black"
                    placeholder="Add keyword"
                    value={newKeyword}
                    onChange={(e) => setNewKeyword(e.target.value)}
                  />
                  <button
                    className="py-2 px-4 bg-[#3F5CFF] hover:bg-[#2544F1] text-white rounded-md"
                    onClick={handleAddKeyword}
                  >
                    Add
                  </button>
                </div>
                <div className="flex flex-wrap gap-2 mb-4">
                  {keywords.map((keyword, index) => (
                    <div key={index} className="flex items-center text-black gap-2 bg-gray-200 px-3 py-1 rounded-md">
                      <span>{keyword}</span>
                      <button
                        className="text-red-500 font-semibold"
                        onClick={() => handleRemoveKeyword(index)}
                      >
                        Remove
                      </button>
                    </div>
                  ))}
                </div>
              </>
            )}

            <textarea
              className="w-full h-32 p-2 border border-gray-300 text-black rounded-md mb-4"
              placeholder={`Enter text to ${activeOption.toLowerCase()}...`}
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
            />
            <button
              className="w-full font-semibold py-2 bg-[#00158E] hover:bg-[#000F63] transition-all text-white rounded-md"
              onClick={() => handleSubmit(activeOption)}
            >
              Submit
            </button>
            {activeOption == 'Validate' ? 
              <>
                {outputText && (
                <div className="mt-8">
                  <h3 className="text-2xl font-semibold text-indigo-800 mb-2">Result</h3>
                  <p className="p-2 bg-gray-100 rounded-md text-black">
                    {outputText.split('\n').map((line, index) => (
                      <React.Fragment key={index}>
                        {line}
                        <br />
                      </React.Fragment>
                    ))}
                  </p>
                </div>
              )}
              </>
            :
              <>
                <div className="mt-8">
                  <h3 className="text-2xl font-semibold text-indigo-800 mb-2">Result</h3>
                  <p className="p-2 bg-gray-100 rounded-md text-black">
                    {outputText}
                  </p>
                </div>
              </>
            }
          </div>
        )}
      </div>
    </div>
  );
};

export default SummarizerPage;
