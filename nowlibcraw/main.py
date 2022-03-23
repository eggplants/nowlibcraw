import argparse
import os
import shutil

from dotenv import load_dotenv

from . import __version__
from .PostTweet import PostTweet
from .TulipsGetNewResource import TulipsGetNewResource


class HelpFormatter(
    argparse.ArgumentDefaultsHelpFormatter, argparse.RawDescriptionHelpFormatter
):
    pass


def check_natural(v: str) -> int:
    if int(v) < 0:
        raise argparse.ArgumentTypeError(f"{repr(v)} is an invalid natural int")
    else:
        return int(v)


def check_isdir(p: str) -> str:
    if os.path.isdir(p):
        return p
    elif os.path.exists(p):
        raise argparse.ArgumentTypeError(f"{repr(p)} is not dir.")
    else:
        os.makedirs(p)
        return p


def check_isfile(p: str) -> str:
    if os.path.isfile(p):
        return p
    else:
        raise argparse.ArgumentTypeError(f"{repr(p)} is not file.")


def parse_args() -> argparse.Namespace:
    """Parse arguments."""
    parser = argparse.ArgumentParser(
        prog="nowlibcraw",
        formatter_class=(
            lambda prog: HelpFormatter(
                prog,
                **{
                    "width": shutil.get_terminal_size(fallback=(120, 50)).columns,
                    "max_help_position": 30,
                },
            )
        ),
        description="Obtaining information about new materials from the library system",
    )
    parser.add_argument(
        "-u",
        "--url",
        metavar="URL",
        type=str,
        help="target url",
        default="https://www.tulips.tsukuba.ac.jp",
    )
    parser.add_argument(
        "-l",
        "--log_dir",
        metavar="DIR",
        type=check_isdir,
        help="log dir",
        default="log",
    )
    parser.add_argument(
        "-k",
        "--key_file",
        metavar="FILE",
        type=check_isfile,
        help="key file",
    )
    parser.add_argument(
        "-s", "--source_dir", type=check_isdir, help="source dir", default="source"
    )
    parser.add_argument(
        "-w",
        "--within",
        type=check_natural,
        help="number of day",
        default=1,
    )
    parser.add_argument(
        "-t", "--tweet", action="store_true", help="post tweet", default=False
    )
    parser.add_argument(
        "-H",
        "--headless",
        action="store_true",
        help="show browser when getting page",
        default=False,
    )
    parser.add_argument(
        "-V", "--version", action="version", version="%(prog)s {}".format(__version__)
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    if args.key_file is not None:
        load_dotenv(args.key_file)
    keys = (
        os.getenv("CONSUMER_KEY", ""),
        os.getenv("CONSUMER_SECRET", ""),
        os.getenv("ACCESS_TOKEN", ""),
        os.getenv("ACCESS_TOKEN_SECRET", ""),
    )
    print(keys)

    if args.url == "https://www.tulips.tsukuba.ac.jp":
        T = TulipsGetNewResource(args.url, source_path=args.source_dir)
    else:
        raise ValueError("not implemented")
    T.set_arrived_within(args.within)
    sources = T.get(headless=args.headless)
    if args.tweet:
        P = PostTweet(keys=keys, tweet_log_path=args.log_dir)
        P.tweet(sources)


if __name__ == "__main__":
    main()
