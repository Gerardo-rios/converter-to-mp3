from abc import ABC, abstractmethod

class ConverterRepository(ABC):
    @abstractmethod
    def download_audio(self, youtube_url: str) -> str:
        pass