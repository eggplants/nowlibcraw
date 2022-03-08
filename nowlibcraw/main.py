import os

from dotenv import load_dotenv  # type: ignore[import]

from .GetNewResource import GetNewResource
from .PostTweet import PostTweet

load_dotenv(os.path.join(os.path.dirname(__file__), ".twitter.keys"))
KEYS = (
    os.getenv("CONSUMER_KEY", ""),
    os.getenv("CONSUMER_SECRET", ""),
    os.getenv("ACCESS_TOKEN", ""),
    os.getenv("ACCESS_TOKEN_SECRET", ""),
)

# TODO: write retrieved data source out to a file {json, html}
# TODO: save as ./source/YY/MM/YYYY-MM-DD.{json,html}
# TODO: write log out to a file `tweet.log`
# TODO: publish package
# TODO: CLI


def main() -> None:
    T = GetNewResource()
    P = PostTweet(keys=KEYS)
    sources = T.get()
    P.tweet(sources)


if __name__ == "__main__":
    main()
