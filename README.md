# nowlibcraw

[![PyPI](https://img.shields.io/pypi/v/nowlibcraw?color=blue)](https://pypi.org/project/nowlibcraw/) [![Maintainability](https://api.codeclimate.com/v1/badges/11802e4aba9c40b8f0c9/maintainability)](https://codeclimate.com/github/eggplants/nowlibcraw/maintainability)

WIP: Obtaining information about new materials from the library system

## Supported Site(s)

- Tulips - <https://www.tulips.tsukuba.ac.jp>

## CLI

```shellsession
$ nowlibcraw -t -H -k .twitter.keys
[get]https://www.tulips.tsukuba.ac.jp/opac/search?arrivedwithin=1&type[]=book&target=local&searchmode=complex&count=100&autoDetail=true, index = 1
[get]0 books
[success]2022-03-23
```

```shellsession
$ nowlibcraw
usage: nowlibcraw [-h] [-u URL] [-l DIR] [-k FILE] [-s DIR] [-w DAY] [-W DAY] [--weekday DAY] [-t] [-H] [-V]
if you want to read long help, type `nowlibcraw -h`

$ nowlibcraw -h
usage: nowlibcraw [-h] [-u URL] [-l DIR] [-k FILE] [-s DIR] [-w DAY] [-W DAY] [--weekday DAY] [-t] [-H] [-V]

Obtaining information about new materials from the library system

optional arguments:
  -h, --help                    show this help message and exit
  -u URL, --url URL             target url (default: https://www.tulips.tsukuba.ac.jp)
  -l DIR, --log_dir DIR         log dir (default: log)
  -k FILE, --key_file FILE      key file (default: None)
  -s DIR, --source_dir DIR      source dir (default: source)
  -w DAY, --within DAY          number of day (default: 1)
  -W DAY, --within_summary DAY  number of day to summary (default: 7)
  --weekday DAY                 a weekday (0-6, mon-sun) to post week summary (default: 6)
  -t, --tweet                   post tweet (default: False)
  -H, --headless                show browser when getting page (default: False)
  -V, --version                 show program's version number and exit
```
