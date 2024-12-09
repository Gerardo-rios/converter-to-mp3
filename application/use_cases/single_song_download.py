from infrastructure.repositories.converter_repository_impl import ConverterRepositoryImpl
from domain.entities.song import Song

async def single_song_download(youtube_url: str) -> Song:
    converter = ConverterRepositoryImpl()
    file_path = converter.download_audio(youtube_url)
    title = file_path.split('/')[-1].split('.')[0] 
    return Song(title=title, file_path=file_path)