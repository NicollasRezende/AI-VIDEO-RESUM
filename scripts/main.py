from download_audio import download_audio as dlwd_aud
from transcribe_audio import transcribe_audio as tr_aud
from scripts.gerar_resumo import gerar_resumo as generate
import os

if not os.path.exists('data'):
    os.makedirs('data')

while True:
    user = input("Resumir video YT\n\nColoque aqui a URL do video: ")
    
    try:
        audio_path, audio_id = dlwd_aud(user)
        print(f"Áudio baixado com ID: {audio_id}")

        video_text = tr_aud(audio_id)
        print("Transcrição concluída.")

        resumo = generate(video_text)
        print("\nResumo:\n", resumo)
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
