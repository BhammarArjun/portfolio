from flask import Flask, render_template, request, send_file
from zyphra import ZyphraClient
import os
from io import BytesIO
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables
load_dotenv()
api_key = os.getenv('ZYPHRA_API_KEY')
client = ZyphraClient(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return {'error': 'No text provided'}, 400

    # Generate audio using Zyphra API
    audio_data = client.audio.speech.create(
        text=text,
        speaking_rate=15,
        mime_type='audio/mp3'
    )

    # Return the audio data as a file
    return send_file(
        BytesIO(audio_data),
        mimetype='audio/mp3',
        as_attachment=True,
        download_name='output.mp3'
    )

if __name__ == '__main__':
    app.run(debug=True)