from __future__ import annotations

from typing import TYPE_CHECKING 

if TYPE_CHECKING:
    from ..client import Client


class Domain:
    def __init__(
        self,
        client: Client,
        domain: str
    ):
        self._client = client
        self._domain = domain