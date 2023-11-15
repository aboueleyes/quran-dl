import json
from dataclasses import dataclass

from loguru import logger


class QuranDownloader:
    @staticmethod
    def list_reciters() -> list[str]:
        with open("data/reciters.json") as f:
            reciters_data = json.load(f)
        logger.info("Getting list of reciters")
        return [
            Reciter(
                name=reciter["name"],
                arabic_name=reciter["arabicName"],
                id=reciter["id"],
                file_name=reciter["relativePath"],
            )
            for reciter in reciters_data.values()
        ]

    @staticmethod
    def get_chapter_path(chapter: int, reciter: "Reciter") -> str:
        return f"https://download.quranicaudio.com/quran/{reciter.file_name}/{chapter:03}.mp3"


@dataclass(frozen=True)
class Reciter:
    name: str
    arabic_name: str
    id: str
    file_name: str
