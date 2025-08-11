from flask import Flask, request, jsonify
from translate import Translator

app = Flask(__name__)

@app.route('/translate', methods=['POST'])
def translate_text():
    '''
        endpoint => http://127.0.0.1:8000/translate
        body=>
        {
            "fl":"en",
            "tl":"hi",
            "text":"hello"
        }~

        get=>
        {
            "translated_text": "नमस्ते"
        }
    '''
    data = request.get_json()
    to_lang = data.get('tl', 'en')
    from_lang = data.get('fl', 'en')
    text = data.get('text','')
    
    translator= Translator(to_lang=to_lang,from_lang=from_lang)
    result = translator.translate(text)
    return jsonify({'translated_text': result})
    

if __name__ == '__main__':
    app.run(debug=True,port=8000,host='0.0.0.0')