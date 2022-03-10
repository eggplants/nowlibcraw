# nowlibcraw

WIP: Obtaining information about new materials from the library system

## Supported Site(s)

- Tulips - <https://www.tulips.tsukuba.ac.jp>

## CLI

```
$ nowlibcraw -h
usage: nowlibcraw [-h] [-u URL] [-l DIR] [-k FILE] [-s SOURCE_DIR] [-t] [-S] [-V]

Obtaining information about new materials from the library system

optional arguments:
  -h, --help                  show this help message and exit
  -u URL, --url URL           target url (default: https://www.tulips.tsukuba.ac.jp)
  -l DIR, --log_dir DIR       log dir (default: log)
  -k FILE, --key_file FILE    key file (default: None)
  -s SOURCE_DIR, --source_dir SOURCE_DIR
                              source dir (default: source)
  -t, --tweet                 post tweet (default: False)
  -S, --show_browser          show browser when getting page (default: False)
  -V, --version               show program's version number and exit
```
