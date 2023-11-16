import os
from argparse import ArgumentParser
from collections.abc import Iterable

from iterfzf import iterfzf
from loguru import logger
from quran_dl import QuranDownloader, RangeParser, Reciter

if __name__ == "__main__":
    arg_parser = ArgumentParser()

    arg_parser.add_argument("--language", default="ar")
    arg_parser.add_argument("--range", "-r", default="1-114", type=str)

    args = arg_parser.parse_args()
    range_: list[int] = RangeParser.parse(args.range)

    reciters: list[Reciter] = QuranDownloader.list_reciters()
    field: str = "name" if args.language == "en" else "arabic_name"

    chosen_reciters_names: Iterable[str] = iterfzf([getattr(reciter, field) for reciter in reciters], multi=True)
    chosen_reciters: list[Reciter] = [
        reciter for reciter in reciters if getattr(reciter, field) in chosen_reciters_names
    ]

    logger.info("Chosen reciters: {}", chosen_reciters)

    os.makedirs("urls", exist_ok=True)

    for reciter in chosen_reciters:
        with open(f"urls/{reciter.name}.txt", "w") as f:
            for chapter in range_:
                f.write(QuranDownloader.get_chapter_path(chapter, reciter) + "\n")

        logger.info("Saved urls for {} to urls/{}.txt", reciter.name, reciter.name)
