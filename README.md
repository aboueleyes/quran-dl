# quran-dl
[![StandWithPalestine](https://raw.githubusercontent.com/TheBSD/StandWithPalestine/main/badges/StandWithPalestine.svg)](https://github.com/TheBSD/StandWithPalestine/blob/main/docs/README.md)


A Python package to download Quran audio files .



## Usage

You can import the module from the package like this:

```bash
> pip install -r requirements.txt
> python src/main.py
```

This will add all urls to a the directory `./urls`, you can then use a download manager to download the files.
or use wget to download the files.

```bash
> wget -i urls/sudais.txt -P ./sudais
```

You can specify the start and end surahs to download.

```bash
> python src/main.py --start 1 --end 2
```

To get a single surah 
```bash
> python src/main.py --s 12 --e 12
```

You can specify the language to use for the download.

```bash
> python src/main.py --lang en
> python src/main.py --lang ar
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.
