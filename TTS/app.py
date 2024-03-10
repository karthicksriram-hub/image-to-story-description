# app.py (Flask Backend)
from flask import Flask, render_template, request, Response
from gtts import gTTS
from googletrans import Translator
import io

app = Flask(__name__)

def get_language_code(language_name):
    # Add more language codes as needed
    language_codes = {
        'English': 'en',
        'Spanish': 'es',
        'French': 'fr',
        'Tamil': 'ta',
        'Hindi': 'hi',
        'Telugu': 'te',
        'Malayalam': 'ml',
        # Add more languages here
    }
    return language_codes.get(language_name, 'en')  # Default to English if not found

def translate_text(text, target_language):
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    return translation.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_speech():
    text_to_say = request.form['text_to_say']
    selected_language = request.form['language']

    language_code = get_language_code(selected_language)
    
    # Translate the text to the selected language
    translated_text = translate_text(text_to_say, language_code)
    
    gtts_object = gTTS(text=translated_text, lang=language_code, slow=False)
    
    # Save the generated speech as a WAV file in memory
    audio_stream = io.BytesIO()
    gtts_object.write_to_fp(audio_stream)
    audio_stream.seek(0)

    return Response(audio_stream, mimetype='audio/wav')

if __name__ == '__main__':
    app.run(debug=True)
