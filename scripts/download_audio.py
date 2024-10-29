import os
import yt_dlp

def download_audio(youtube_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'data/%(id)s.%(ext)s',
        'ffmpeg_location': 'C:\\Users\\nicollas\\Documents\\ffmpeg-2024-10-27-git-bb57b78013-full_build\\bin',
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            },
        ],
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)
        audio_id = info['id']
        
        # Construa o caminho do arquivo
        audio_path = f"data/{audio_id}.mp3"
        
        # Verifique se o arquivo foi criado
        if not os.path.isfile(audio_path):
            raise FileNotFoundError(f"Arquivo de áudio não encontrado: {audio_path}")

    return audio_path, audio_id  # Retorne o caminho do arquivo e o ID
