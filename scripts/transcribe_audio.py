import os
import whisper

def transcribe_audio(audio_id):
    audio_path = f"data/{audio_id}.mp3"
    
    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {audio_path}")
    
    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    return result['text']
