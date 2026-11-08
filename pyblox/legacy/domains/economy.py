from __future__ import annotations

from typing import TYPE_CHECKING

from .domain import Domain

if TYPE_CHECKING:
    from ..client import Client


class EconomyDomain(Domain):
    def __init__(self, client: Client):
        super().__init__(client, "https://economy.roblox.com")

    async def get_group_transactions_v2(
        self,
        group_id: int,
        key: int,
        sort_order: str,
        paging_direction: str,
        page_number: int,
        discriminator: str,
        count: int,
        transaction_type: str
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v2/groups/{group_id}/transactions",
            params={
                "exclusiveStartRequest": {
                    "key": key,
                    "sortOrder": sort_order,
                    "pagingDirection": paging_direction,
                    "pageNumber": page_number,
                    "discriminator": discriminator,
                    "count": count
                },
                "transactionType": transaction_type
            },
            use_cookie=True
        )
        return data

    async def get_group_revenue_summary_v1(
        self,
        group_id: int,
        time_frame: str
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/groups/{group_id}/revenue/summary/{time_frame}",
            use_cookie=True
        )
        return data

    async def get_user_currency_v1(self) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v1/user/currency",
            use_cookie=True
        )
        return data

    async def sales_report_download_v2(
        self,
        target_id: int,
        target_type: str,
        start_date: str,
        end_date: str,
        transaction_type: str
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v2/sales-report/download",
            params={
                "targetId": target_id,
                "targetType": target_type,
                "startDate": start_date,
                "endDate": end_date,
                "transactionType": transaction_type
            },
            use_cookie=True
        )
        return data

    async def get_user_transactions_totals_v2(
        self,
        user_id: int,
        used_types: str,
        time_frame: str,
        transaction_type: str,

        key: int,
        sort_order: str,
        paging_direction: str,
        page_number: int,
        discriminator: str,
        count: int
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v2/users/{user_id}/transactions/totals",
            params={
                "usedTypes": used_types,
                "timeFrame": time_frame,
                "transactionType": transaction_type,
                "exclusiveStartRequest": {
                    "key": key,
                    "sortOrder": sort_order,
                    "pagingDirection": paging_direction,
                    "pageNumber": page_number,
                    "discriminator": discriminator,
                    "count": count
                }
            },
            use_cookie=True
        )
        return data

    async def get_user_transaction_types_v2(
        self,
        user_id: int
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v2/users/{user_id}/transaction-types",
            use_cookie=True
        )
        return data

    async def get_user_transactions_v2(
        self,
        user_id: int,
        key: int,
        sort_order: str,
        paging_direction: str,
        page_number: int,
        discriminator: str,
        count: int
    ) -> dict:
        data = await self._client.http.request(
            method="GET",
            url=f"{self._domain}/v2/users/{user_id}/transactions",
            params={
                "exclusiveStartRequest": {
                    "key": key,
                    "sortOrder": sort_order,
                    "pagingDirection": paging_direction,
                    "pageNumber": page_number,
                    "discriminator": discriminator,
                    "count": count
                }
            },
            use_cookie=True
        )
        return data