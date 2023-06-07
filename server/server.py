from flask import Flask, request, jsonify
from my_translation_package import my_translator

app = Flask(__name__)

@app.route('/translate/english_to_french', methods=['POST'])
def translate_english_to_french():
    text = request.json['text']
    return jsonify(my_translator.english_to_french(text))

@app.route('/translate/french_to_english', methods=['POST'])
def translate_french_to_english():
    text = request.json['text']
    return jsonify(my_translator.french_to_english(text))

if __name__ == '__main__':
    app.run()
