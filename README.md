# Flask Translation App

A simple Flask web application that translates English text to Finnish using the `Helsinki-NLP/opus-mt-en-fi` model from Hugging Face's Transformers library.

## Features

- Input field to enter text in English.
- A button to submit and translate text to Finnish.
- Translation powered by Hugging Face's pre-trained model.

## Prerequisites

Ensure the following are installed on your machine:

- **Python 3.6+**: Check by running `python --version` in the terminal.
- **pip**: Python’s package installer (comes with Python by default).

## Installation

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/flask-translation-app.git
cd flask-translation-app
```
### 2. Set Up a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.
On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```
### 3. Install Dependencies
Once the virtual environment is activated, install the required dependencies:

```bash
pip install flask transformers torch tensorflow sentencepiece
```

### 4. Install PyTorch or TensorFlow
Since the translation model uses either TensorFlow or PyTorch, you must install one of them:

For PyTorch
```bash
pip install torch
```

For TensorFlow
```bash
pip install torch
```

### 5. Set Up the Hugging Face Model
We will use the Helsinki-NLP/opus-mt-en-fi model for translation. The transformers library will automatically handle the model download when the app is run.

### 6. Running the Application
Once everything is set up, run the Flask application:

```bash
python app.py
```
