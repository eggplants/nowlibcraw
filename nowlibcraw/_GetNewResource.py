from __future__ import annotations

from abc import ABCMeta, abstractmethod
from typing import Any

from .Dicts import BookData


class GetNewResource(metaclass=ABCMeta):
    @abstractmethod
    def __init__(
        self, base_url: str, params: dict[str, Any], source_path: str, user_agent: str
    ) -> None:
        pass

    @abstractmethod
    def get(self, headless: bool) -> list[BookData]:
        pass

    @abstractmethod
    def _save_data(self, data: list[BookData]) -> None:
        pass

    @abstractmethod
    async def _get_pages(self, headless: bool) -> list[str]:
        pass

    @abstractmethod
    async def _get_page(self, page: Any, page_index: int) -> tuple[str | None, bool]:
        pass

    @abstractmethod
    def _extract_json(self, sources: list[str]) -> list[BookData]:
        pass
