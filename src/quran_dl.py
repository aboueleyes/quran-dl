import json
import re
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


class RangeParser:
    """Given a string specifying a range of numbers, return a list of numbers.
    >>> RangeParser.parse("1-3")
    [1, 2, 3]
    >>> RangeParser.parse("1,3,5")
    [1, 3, 5]
    >>> RangeParser.parse("1")
    [1]
    >>> RangeParser.parse("1-3,10-13")
    [1, 2, 3, 10, 11, 12, 13]
    >>> RangeParser.parse("1-3 10-13")
    [1, 2, 3, 10, 11, 12, 13]
    """

    DELIMITER = re.compile(r"[,\s]")

    @classmethod
    def parse(cls, range_string) -> list[int]:
        return [
            number
            for range_ in re.split(cls.DELIMITER, cls._clean_string(range_string))
            for number in cls._parse_range(range_)
        ]

    @staticmethod
    def _parse_range(range_: str) -> list[int]:
        if "-" in range_:
            start, end = range_.split("-")
            return list(range(int(start), int(end) + 1))
        return [int(range_)]

    @staticmethod
    def _clean_string(range_string: str) -> str:
        range_string = range_string.strip()
        return " ".join(range_string.split())
