"""
Import the package machinetranslation in server.py.
"""
import json
from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/englishToFrench")
def english_to_french():
    """
    This function takes the English text as input through the
    request parameter and return a string.
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    english_text= translator.french_to_english(text_to_translate)
    return english_text

@app.route("/frenchToEnglish")
def french_to_english():
    """
    This function takes the French text as input through the
    request parameter and return a string.
    """
    text_to_translate = request.args.get('textToTranslate')
    # Write your code here
    french_text= translator.french_to_english(text_to_translate)
    return french_text

@app.route("/")
def render_index_page():
    """
    This function renders the index.html.
    """
    # Write the code to render template
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

