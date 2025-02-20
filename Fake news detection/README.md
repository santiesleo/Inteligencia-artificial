![ICESI University Logo](https://res.cloudinary.com/dxhi8xsyb/image/upload/v1731991202/ICESI_logo_prin_descriptor_RGB_POSITIVO_0924_bszq4w.png)

# Computing and Discrete Structures III - Software Engineering

# Formal foundations and neural applications of turing machines in natural language processing and fake news detection

## Team members

- Dylan Bermúdez Cardona
- Juan David Calderón Salamanca
- Santiago Escobar León

---

## Overview

The **Turing Machine Formalization and Neural NLP System** is designed to explore Turing Machines as language recognizers and function calculators, implement machine learning basics with a focus on natural language processing (NLP), and apply neural networks to tackle the classification of fake news. This system leverages concepts such as supervised learning, Dense Neural Networks, Recurrent Neural Networks (RNN), and Long Short-Term Memory (LSTM) to classify articles using a labeled dataset.

> [!NOTE]  
> *Reference: Bird, Steven, Edward Loper, and Ewan Klein (2009), Natural Language Processing with Python. O’Reilly Media Inc.*

## Step-by-Step Program Outline

1. **Formal Definition of a Turing Machine**:
   - **Objective**: Define the theoretical basis of a Turing Machine and its components.
   - **Implementation**: Construct Turing Machines within a Python-based framework to recognize languages and calculate functions, reinforcing foundational computer science concepts.

2. **Dataset Gathering and Preprocessing (Supervised Learning)**:
   - **Objective**: Collect a labeled dataset of fake news articles, preprocess the data, and prepare it for training.
   - **Implementation**: Use `nltk` for tokenization, lowercasing, and stopword removal, ensuring clean and structured input for model training.

3. **Baseline Model (DummyClassifier)**:
   - **Objective**: Establish a baseline for fake news classification performance.
   - **Implementation**: Train and evaluate a `DummyClassifier` on the dataset, measuring accuracy, precision, recall, and F1-score to benchmark against more complex models.

4. **Dense Neural Network Model**:
   - **Objective**: Implement a Dense Neural Network to classify articles as reliable or unreliable.
   - **Implementation**: Train and tune a Dense Neural Network on the preprocessed data, optimizing hyperparameters using tools like `GridSearchCV` and evaluating accuracy, precision, recall, F1-score, and kappa score.

5. **Vanilla RNN Model**:
   - **Objective**: Build and test a simple RNN model for fake news detection.
   - **Implementation**: Train and tune the model on the dataset, optimizing its performance and evaluating the results using standard classification metrics.

6. **LSTM Model for Improved Text Classification**:
   - **Objective**: Leverage an LSTM model for better sequence handling and context understanding in fake news detection.
   - **Implementation**: Train, tune, and evaluate an LSTM model, measuring performance metrics and comparing results to assess the model's effectiveness in fake news classification.

### NLP and Neural Network Concepts
The system applies several advanced NLP and neural network concepts to handle the complexities of text data:
   - **Natural Language Processing (NLP)**: Basic processing using supervised learning for fake news detection.
   - **Recurrent Neural Networks (RNN) and LSTM**: Application of RNN and LSTM architectures to understand temporal patterns within article content.
   - **Turing Neural Networks**: Integration of Turing machine principles within neural network contexts for theoretical explorations of computational limits in NLP tasks.

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
scikit-learn==1.1.0
```

## Running the System

To start the backend, navigate to the backend directory and execute:

```bash
turing-nlp-project\src\backend> python -m uvicorn app:app --reload
```

To start the frontend, navigate to the frontend directory and execute:

```bash
turing-nlp-project\src\frontend> npm run dev
```

## **Developed with** 🛠️

<div style="text-align: left">
    <p>
        <a href="https://code.visualstudio.com/" target="_blank"> <img alt="Visual Studio Code" src="https://cdn.svgporn.com/logos/visual-studio-code.svg" height="60" width = "60"></a>
        <a href="https://www.tensorflow.org/?hl=es-419" target="_blank"> <img alt="TensorFlow" src="https://cdn.svgporn.com/logos/tensorflow.svg" height="60" width = "60"></a>
        <a href="https://pandas.pydata.org/" target="_blank"> <img alt="Pandas" src="https://cdn.svgporn.com/logos/pandas-icon.svg" height="60" width = "60"></a>
        <a href="https://numpy.org/" target="_blank"> <img alt="Numpy" src="https://cdn.svgporn.com/logos/numpy.svg" height="60" width = "60"></a>
        <a href="https://pytorch.org/" target="_blank"> <img alt="PyTorch" src="https://cdn.svgporn.com/logos/pytorch-icon.svg" height="60" width = "60"></a>
    </p>
</div>
