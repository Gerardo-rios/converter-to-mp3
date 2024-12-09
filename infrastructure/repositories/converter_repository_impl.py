import yt_dlp
from domain.repositories.converter_repository import ConverterRepository

class ConverterRepositoryImpl(ConverterRepository):
    def download_audio(self, youtube_url: str) -> str:
        output_path = "downloads/%(title)s.%(ext)s"
        options = {
            'format': 'bestaudio/best',
            'outtmpl': output_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'quiet': True,
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download([youtube_url])
        return output_path