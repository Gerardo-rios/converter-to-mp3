from pydantic import BaseModel

class Song(BaseModel):
    title: str
    file_path: str