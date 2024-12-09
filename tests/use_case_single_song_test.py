import pytest
from application.use_cases.single_song_download import single_song_download
from domain.entities.song import Song

@pytest.mark.asyncio
async def test_single_song_download():
    youtube_url = "https://www.youtube.com/watch?v=0OcihKnTp9M"
    response = await single_song_download(youtube_url)
    assert isinstance(response, Song)
    assert response.file_path.endswith(".mp3")
    assert response.message == "Download successful"