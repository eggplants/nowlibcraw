# nowlibcraw

WIP: Obtaining information about new materials from the library system

## Supported Site(s)

- Tulips - <https://www.tulips.tsukuba.ac.jp>

## CLI

```shellsession
$ nowlibcraw -h
usage: nowlibcraw [-h] [-u URL] [-l DIR] [-k FILE] [-s DIR] [-w DAY] [-W DAY] [-t] [-H] [-V]

Obtaining information about new materials from the library system

optional arguments:
  -h, --help                    show this help message and exit
  -u URL, --url URL             target url (default: https://www.tulips.tsukuba.ac.jp)
  -l DIR, --log_dir DIR         log dir (default: log)
  -k FILE, --key_file FILE      key file (default: None)
  -s DIR, --source_dir DIR      source dir (default: source)
  -w DAY, --within DAY          number of day (default: 1)
  -W DAY, --within_summary DAY  number of day to summary (default: 7)
  -t, --tweet                   post tweet (default: False)
  -H, --headless                show browser when getting page (default: False)
  -V, --version                 show program's version number and exit

```
