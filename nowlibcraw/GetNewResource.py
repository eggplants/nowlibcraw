import asyncio
from typing import List, Optional, Tuple

import pyppeteer  # type: ignore[import]
from bs4 import BeautifulSoup as BS  # type: ignore[import]
from bs4.element import ResultSet, Tag  # type: ignore[import]

from .Dicts import BookData, TulipsParams


class GetNewResource:
    _default_params: TulipsParams = {
        "arrivedwithin": 1,
        "type": "book",
        "target": "local",
        "searchmode": "complex",
        "count": 100,
    }

    def __init__(
        self,
        base_url: str = "https://www.tulips.tsukuba.ac.jp",
        params: TulipsParams = _default_params,
    ) -> None:
        self.base_url = base_url
        self.params = params

    def get(self) -> List[BookData]:
        sources = asyncio.get_event_loop().run_until_complete(self._get_pages())
        return self._extract_json(sources)

    async def _get_pages(self) -> List[str]:
        browser = await pyppeteer.launch(
            # headless=False
        )
        contents: List[str] = []
        page = await browser.newPage()
        content, next_url = asyncio.get_event_loop().run_until_complete(
            self._get_page(page)
        )
        contents.append(content)
        while next_url is not None:
            content, next_url = asyncio.get_event_loop().run_until_complete(
                self._get_page(page)
            )
            contents.append(content)

        await browser.close()
        return contents

    async def _get_page(self, page: pyppeteer.Page) -> Tuple[str, Optional[str]]:
        await page.goto(
            self.base_url
            + "/opac/search?"
            + "&".join(
                [
                    f"{k if k != 'type' else 'type[]'}={v}"
                    for k, v in self.params.items()
                ]
            ),
            {"waitUntil": "networkidle0"},
        )
        content = str(await page.content())
        next_url = BS(content).find("input", class_="l_volume_page_next")
        if isinstance(next_url, Tag) and hasattr(next_url, "value"):
            return content, str(next_url.value)
        else:
            return content, None

    def _extract_json(self, sources: List[str]) -> List[BookData]:
        def get_book_info_text(book: Optional[Tag], class_: str) -> str:
            if book is None:
                return ""
            b = book.find("dl", class_=class_)
            if (
                hasattr(b, "dd")
                and isinstance(b, Tag)
                and hasattr(b.dd, "span")
                and isinstance(b.dd, Tag)
                and isinstance(b.dd.span, Tag)
                and hasattr(b.dd.span, "text")
            ):
                return str(b.dd.span.text)
            else:
                return ""

        res: List[BookData] = []
        for source_idx, source in enumerate(sources):
            b = BS(source)
            books: ResultSet = b.select(
                "div.panel.searchCard.l_searchCard.c_search_card.p_search_card"
            )
            default_img = "/bookimage-kango.png"
            for book_idx, book_d in enumerate(books):
                book = book_d.select_one(
                    "div.informationArea.c_information_area.l_informationArea"
                )
                res_i: BookData = {
                    "index": source_idx * 100 + book_idx,
                    "data": {
                        "link": "",
                        "title": "",
                        "author": "",
                        "publisher": "",
                        "isbn": "",
                        "holding": "",
                        "status": "",
                        "imagesrc": "",
                    },
                }
                h3 = (
                    book.h3.a
                    if hasattr(book, "h3")
                    and isinstance(book, Tag)
                    and hasattr(book.h3, "a")
                    and isinstance(book.h3, Tag)
                    else None
                )
                res_i["data"]["link"] = (
                    "" if h3 is None else self.base_url + str(h3.get("href"))
                )
                res_i["data"]["title"] = "" if h3 is None else h3.text
                res_i["data"]["author"] = get_book_info_text(
                    book, "l_detail_info_au_book"
                )
                res_i["data"]["publisher"] = get_book_info_text(
                    book, "l_detail_info_pu"
                )
                res_i["data"]["isbn"] = get_book_info_text(book, "l_detail_info_sb")
                res_i["data"]["holding"] = get_book_info_text(book, "l_detail_info_hd")
                res_i["data"]["status"] = get_book_info_text(book, "l_detail_info_st")
                img = book_d.select_one("img")
                imgsrc = None if img is None else img.get("src")
                res_i["data"]["imagesrc"] = (
                    ""
                    if type(imgsrc) is not str or imgsrc[-20:] != default_img
                    else imgsrc
                )
                res.append(res_i)
        else:
            return res
