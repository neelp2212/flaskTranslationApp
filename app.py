from flask import Flask, request, jsonify, render_template
from transformers import pipeline

# Initialize Flask app
app = Flask(__name__)

# Load the translation pipeline
translator = pipeline("translation_en_to_fi", model="Helsinki-NLP/opus-mt-en-fi")

@app.route('/')
def index():
    # Render the HTML form
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    # Get text from the form
    text_to_translate = request.form['text']
    if not text_to_translate:
        return jsonify({"error": "No text provided"}), 400
    
    # Translate the text
    translated_text = translator(text_to_translate)[0]['translation_text']
    
    # Return the result
    return jsonify({"original": text_to_translate, "translated": translated_text})

if __name__ == "__main__":
    app.run(debug=True)
