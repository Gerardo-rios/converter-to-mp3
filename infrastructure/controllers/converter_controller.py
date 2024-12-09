from fastapi import APIRouter, HTTPException
from application.use_cases.single_song_download import single_song_download
from domain.entities.song import Song

router = APIRouter()

@router.post("/single_song_download", response_model=Song)
async def download_single_song(youtube_url: str):
    try:
        return await single_song_download(youtube_url)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))